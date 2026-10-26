"""
主程序入口，启动QQ机器人和DeepSeek对话服务。
"""
import asyncio
import logging
import signal
import sys
from typing import Optional

from config import config
from deepseek_client import DeepSeekClient
from qq_client import QQClient
from message_handler import MessageHandler

logger = logging.getLogger(__name__)

# 配置日志
logging.basicConfig(
    level=logging.DEBUG if config.DEBUG else logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler("qq_gf.log", encoding="utf-8")
    ]
)

class QQGirlfriendBot:
    """QQ电子女友机器人"""
    
    def __init__(self):
        self.deepseek_client: Optional[DeepSeekClient] = None
        self.qq_client: Optional[QQClient] = None
        self.message_handler: Optional[MessageHandler] = None
        self.running = False
        self.tasks = []
    
    async def initialize(self):
        """初始化客户端"""
        logger.info("正在初始化机器人...")
        
        # 初始化DeepSeek客户端
        self.deepseek_client = DeepSeekClient()
        # 初始化QQ客户端
        self.qq_client = QQClient()
        
        # 测试连接
        try:
            async with self.deepseek_client as ds, self.qq_client as qq:
                # 测试DeepSeek连接
                test_reply = await ds.chat([{"role": "user", "content": "你好"}])
                logger.info(f"DeepSeek 连接测试成功: {test_reply[:30]}...")
                
                # 测试QQ连接
                login_info = await qq.get_login_info()
                logger.info(f"QQ 连接测试成功: 登录账号 {login_info.get('data', {}).get('user_id')}")
        except Exception as e:
            logger.error(f"初始化测试失败: {e}")
            raise
        
        # 创建消息处理器
        self.message_handler = MessageHandler(self.deepseek_client, self.qq_client)
        logger.info("初始化完成")
    
    async def run(self):
        """运行主循环"""
        self.running = True
        
        # 启动WebSocket监听（或HTTP轮询）
        # 这里使用WebSocket，如果未配置则使用HTTP轮询
        ws_url = config.GO_CQHTTP_WS_URL
        if ws_url and ws_url.startswith("ws://"):
            listener_task = asyncio.create_task(self.qq_client.listen_events_via_websocket())
            logger.info("使用 WebSocket 监听事件")
        else:
            listener_task = asyncio.create_task(self.qq_client.listen_events_via_http(interval=1.0))
            logger.info("使用 HTTP 轮询监听事件")
        
        # 启动会话清理任务（可选）
        cleanup_task = asyncio.create_task(self.message_handler.cleanup_inactive_sessions())
        
        self.tasks = [listener_task, cleanup_task]
        
        logger.info("QQ电子女友机器人已启动，等待消息...")
        
        # 等待信号
        await self._wait_for_signal()
    
    async def _wait_for_signal(self):
        """等待终止信号"""
        loop = asyncio.get_event_loop()
        stop_event = asyncio.Event()
        
        def signal_handler():
            logger.info("收到停止信号，正在关闭...")
            stop_event.set()
        
        for sig in (signal.SIGINT, signal.SIGTERM):
            loop.add_signal_handler(sig, signal_handler)
        
        await stop_event.wait()
        await self.shutdown()
    
    async def shutdown(self):
        """关闭资源"""
        logger.info("正在关闭机器人...")
        self.running = False
        
        # 取消所有任务
        for task in self.tasks:
            task.cancel()
        
        # 等待任务结束
        await asyncio.gather(*self.tasks, return_exceptions=True)
        
        # 关闭客户端
        if self.qq_client and self.qq_client.session:
            await self.qq_client.session.close()
        if self.deepseek_client and self.deepseek_client.session:
            await self.deepseek_client.session.close()
        
        logger.info("机器人已关闭")

async def main():
    """主函数"""
    bot = QQGirlfriendBot()
    
    try:
        await bot.initialize()
        await bot.run()
    except KeyboardInterrupt:
        logger.info("用户中断")
    except Exception as e:
        logger.exception(f"机器人运行异常: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    # 检查配置
    if not config.DEEPSEEK_API_KEY:
        print("错误: 未设置 DeepSeek API 密钥")
        print("请设置环境变量 DEEPSEEK_API_KEY 或修改 config.py 文件")
        sys.exit(1)
    
    if config.SELF_QQ_ID == 0:
        print("警告: SELF_QQ_ID 未设置，将无法过滤自身消息")
    
    print("=" * 50)
    print("QQ电子女友机器人")
    print(f"DeepSeek 模型: {config.DEEPSEEK_MODEL}")
    print(f"系统提示: {config.SYSTEM_PROMPT[:50]}...")
    print("=" * 50)
    
    # 运行
    exit_code = asyncio.run(main())
    sys.exit(exit_code)