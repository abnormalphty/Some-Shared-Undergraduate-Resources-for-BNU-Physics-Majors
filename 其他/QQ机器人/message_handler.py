"""
消息处理器，负责协调QQ消息和DeepSeek回复。
维护用户对话历史，并调用相应客户端。
"""
import asyncio
import logging
import json
from typing import Dict, Any, Optional, List
from dataclasses import dataclass, field
from collections import defaultdict

from config import config
from deepseek_client import DeepSeekClient
from qq_client import QQClient

logger = logging.getLogger(__name__)

@dataclass
class UserSession:
    """用户会话数据"""
    user_id: int
    history: List[Dict[str, str]] = field(default_factory=list)
    last_active: float = field(default_factory=lambda: asyncio.get_event_loop().time())

class MessageHandler:
    """消息处理器"""
    
    def __init__(self, deepseek_client: DeepSeekClient, qq_client: QQClient):
        self.deepseek = deepseek_client
        self.qq = qq_client
        self.sessions: Dict[int, UserSession] = {}
        # 添加消息处理器到QQ客户端
        self.qq.add_message_handler(self.handle_event)
    
    def get_session(self, user_id: int) -> UserSession:
        """获取或创建用户会话"""
        if user_id not in self.sessions:
            self.sessions[user_id] = UserSession(user_id=user_id)
        return self.sessions[user_id]
    
    def handle_event(self, event: Dict[str, Any]):
        """处理QQ事件（同步函数，内部调用异步）"""
        # 在事件循环中调度异步处理
        asyncio.create_task(self._handle_event_async(event))
    
    async def _handle_event_async(self, event: Dict[str, Any]):
        """异步处理事件"""
        try:
            post_type = event.get("post_type")
            if post_type != "message":
                return
            
            message_type = event.get("message_type")
            if message_type == "private":
                await self._handle_private_msg(event)
            elif message_type == "group":
                await self._handle_group_msg(event)
            else:
                logger.debug(f"忽略未知消息类型: {message_type}")
        except Exception as e:
            logger.exception(f"处理事件时发生异常: {e}")
    
    async def _handle_private_msg(self, event: Dict[str, Any]):
        """处理私聊消息"""
        user_id = event.get("user_id")
        raw_message = event.get("raw_message", "")
        message_id = event.get("message_id")
        
        logger.info(f"收到私聊消息 [{user_id}]: {raw_message}")
        
        # 过滤空消息
        if not raw_message.strip():
            return
        
        # 获取用户会话
        session = self.get_session(user_id)
        session.last_active = asyncio.get_event_loop().time()
        
        # 调用DeepSeek生成回复
        async with self.deepseek as client:
            reply = await client.chat_with_history(raw_message, session.history)
        
        # 更新历史记录
        session.history.append({"role": "user", "content": raw_message})
        session.history.append({"role": "assistant", "content": reply})
        
        # 限制历史记录长度
        if len(session.history) > config.MAX_HISTORY * 2:  # 每轮对话包含 user 和 assistant 两条
            session.history = session.history[-config.MAX_HISTORY * 2:]
        
        # 发送回复
        resp = await self.qq.send_private_msg(user_id, reply)
        if resp.get("status") == "ok":
            logger.info(f"已回复 [{user_id}]: {reply[:50]}...")
        else:
            logger.error(f"回复失败: {resp}")
    
    async def _handle_group_msg(self, event: Dict[str, Any]):
        """处理群聊消息（可选：只在被@时回复）"""
        group_id = event.get("group_id")
        user_id = event.get("user_id")
        raw_message = event.get("raw_message", "")
        
        # 判断是否@了机器人
        self_id = config.SELF_QQ_ID
        if self_id and f"[CQ:at,qq={self_id}]" in raw_message:
            # 移除@标记
            cleaned_msg = raw_message.replace(f"[CQ:at,qq={self_id}]", "").strip()
            if not cleaned_msg:
                cleaned_msg = "你好"
            
            logger.info(f"收到群聊@消息 [{group_id}] [{user_id}]: {cleaned_msg}")
            
            # 调用DeepSeek生成回复
            async with self.deepseek as client:
                reply = await client.chat_with_history(cleaned_msg, [])
            
            # 回复时@对方
            reply_msg = f"[CQ:at,qq={user_id}] {reply}"
            await self.qq.send_group_msg(group_id, reply_msg)
    
    async def cleanup_inactive_sessions(self, timeout: float = 3600):
        """清理不活跃的会话（可选）"""
        while True:
            await asyncio.sleep(300)  # 每5分钟检查一次
            now = asyncio.get_event_loop().time()
            to_delete = []
            for user_id, session in self.sessions.items():
                if now - session.last_active > timeout:
                    to_delete.append(user_id)
            
            for user_id in to_delete:
                del self.sessions[user_id]
                logger.debug(f"清理不活跃会话: {user_id}")

# 单例处理器
async def get_message_handler() -> MessageHandler:
    """获取消息处理器实例"""
    async with DeepSeekClient() as deepseek, QQClient() as qq:
        return MessageHandler(deepseek, qq)

if __name__ == "__main__":
    # 简单测试
    import asyncio
    async def test():
        async with DeepSeekClient() as deepseek, QQClient() as qq:
            handler = MessageHandler(deepseek, qq)
            # 模拟一个事件
            event = {
                "post_type": "message",
                "message_type": "private",
                "user_id": 123456,
                "raw_message": "你好",
                "message_id": 1
            }
            await handler._handle_event_async(event)
    
    asyncio.run(test())