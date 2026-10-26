"""
QQ客户端，通过 go-cqhttp 的 HTTP API 发送和接收消息。
支持 WebSocket 事件监听（可选）。
"""
import aiohttp
import json
import logging
import asyncio
from typing import Dict, Any, Optional, Callable, List
from config import config

logger = logging.getLogger(__name__)

class QQClient:
    """QQ客户端，封装 go-cqhttp 的 HTTP API"""
    
    def __init__(self, base_url: str = None, self_qq_id: int = None):
        self.base_url = base_url or config.GO_CQHTTP_URL
        self.self_qq_id = self_qq_id or config.SELF_QQ_ID
        self.session: Optional[aiohttp.ClientSession] = None
        self.ws: Optional[aiohttp.ClientWebSocketResponse] = None
        self.message_handlers: List[Callable[[Dict[str, Any]], None]] = []
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def send_private_msg(self, user_id: int, message: str, auto_escape: bool = False) -> Dict[str, Any]:
        """
        发送私聊消息。
        
        Args:
            user_id: 对方QQ号
            message: 消息内容
            auto_escape: 是否转义CQ码
        
        Returns:
            API响应
        """
        url = f"{self.base_url}/send_private_msg"
        payload = {
            "user_id": user_id,
            "message": message,
            "auto_escape": auto_escape
        }
        try:
            async with self.session.post(url, json=payload) as resp:
                return await resp.json()
        except Exception as e:
            logger.exception(f"发送私聊消息失败: {e}")
            return {"status": "error", "retcode": -1, "msg": str(e)}
    
    async def send_group_msg(self, group_id: int, message: str, auto_escape: bool = False) -> Dict[str, Any]:
        """
        发送群聊消息。
        
        Args:
            group_id: 群号
            message: 消息内容
            auto_escape: 是否转义CQ码
        
        Returns:
            API响应
        """
        url = f"{self.base_url}/send_group_msg"
        payload = {
            "group_id": group_id,
            "message": message,
            "auto_escape": auto_escape
        }
        try:
            async with self.session.post(url, json=payload) as resp:
                return await resp.json()
        except Exception as e:
            logger.exception(f"发送群消息失败: {e}")
            return {"status": "error", "retcode": -1, "msg": str(e)}
    
    async def get_login_info(self) -> Dict[str, Any]:
        """获取登录号信息"""
        url = f"{self.base_url}/get_login_info"
        async with self.session.get(url) as resp:
            return await resp.json()
    
    def add_message_handler(self, handler: Callable[[Dict[str, Any]], None]):
        """添加消息处理器"""
        self.message_handlers.append(handler)
    
    async def listen_events_via_http(self, interval: float = 1.0):
        """
        通过HTTP轮询获取事件（简单实现，生产环境建议用WebSocket）。
        
        Args:
            interval: 轮询间隔（秒）
        """
        url = f"{self.base_url}/get_latest_events"
        params = {"timeout": int(interval * 1000)}
        
        while True:
            try:
                async with self.session.get(url, params=params) as resp:
                    if resp.status == 200:
                        events = await resp.json()
                        if events and events.get("data"):
                            for event in events["data"]:
                                await self._handle_event(event)
                    else:
                        logger.warning(f"获取事件失败: {resp.status}")
            except Exception as e:
                logger.exception(f"轮询事件异常: {e}")
            
            await asyncio.sleep(interval)
    
    async def listen_events_via_websocket(self):
        """
        通过WebSocket监听事件（推荐）。
        需要 go-cqhttp 启用 WebSocket 服务器。
        """
        ws_url = config.GO_CQHTTP_WS_URL
        if not ws_url:
            raise ValueError("未配置 WebSocket URL")
        
        try:
            async with self.session.ws_connect(ws_url) as ws:
                self.ws = ws
                async for msg in ws:
                    if msg.type == aiohttp.WSMsgType.TEXT:
                        event = json.loads(msg.data)
                        await self._handle_event(event)
                    elif msg.type == aiohttp.WSMsgType.ERROR:
                        logger.error(f"WebSocket 错误: {ws.exception()}")
                        break
                    elif msg.type == aiohttp.WSMsgType.CLOSED:
                        logger.warning("WebSocket 连接关闭")
                        break
        except Exception as e:
            logger.exception(f"WebSocket 连接失败: {e}")
    
    async def _handle_event(self, event: Dict[str, Any]):
        """处理事件，分发给处理器"""
        # 过滤自身消息
        if event.get("self_id") == self.self_qq_id:
            return
        
        # 只处理消息事件
        if event.get("post_type") == "message":
            logger.debug(f"收到消息事件: {event}")
            for handler in self.message_handlers:
                try:
                    handler(event)
                except Exception as e:
                    logger.exception(f"消息处理器异常: {e}")

# 单例客户端
async def get_qq_client() -> QQClient:
    """获取QQ客户端实例（异步上下文管理器）"""
    return QQClient()

if __name__ == "__main__":
    # 简单测试
    import asyncio
    async def test():
        async with QQClient() as client:
            info = await client.get_login_info()
            print("登录信息:", info)
    
    asyncio.run(test())