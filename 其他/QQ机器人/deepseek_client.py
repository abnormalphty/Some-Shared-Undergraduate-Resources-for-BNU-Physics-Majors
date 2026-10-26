"""
DeepSeek API 客户端，用于发送消息并获取回复。
"""
import aiohttp
import json
import logging
from typing import List, Dict, Any, Optional
from config import config

logger = logging.getLogger(__name__)

class DeepSeekClient:
    """DeepSeek API 客户端"""
    
    def __init__(self, api_key: str = None, base_url: str = None, model: str = None):
        self.api_key = api_key or config.DEEPSEEK_API_KEY
        self.base_url = base_url or config.DEEPSEEK_API_BASE
        self.model = model or config.DEEPSEEK_MODEL
        self.session: Optional[aiohttp.ClientSession] = None
        
        if not self.api_key:
            raise ValueError("DeepSeek API密钥未设置，请设置环境变量 DEEPSEEK_API_KEY 或修改配置文件")
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers={
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        })
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def chat(self, messages: List[Dict[str, str]], **kwargs) -> str:
        """
        发送对话消息到DeepSeek API并返回回复文本。
        
        Args:
            messages: 消息列表，每个元素为 {"role": "user"/"assistant"/"system", "content": "..."}
            **kwargs: 其他API参数（如temperature, max_tokens等）
        
        Returns:
            助手回复的文本内容
        """
        url = f"{self.base_url}/chat/completions"
        payload = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "temperature": kwargs.get("temperature", 0.7),
            "max_tokens": kwargs.get("max_tokens", 2000),
        }
        
        try:
            async with self.session.post(url, json=payload) as response:
                if response.status != 200:
                    text = await response.text()
                    logger.error(f"DeepSeek API 错误: {response.status} - {text}")
                    raise Exception(f"API 错误 {response.status}: {text}")
                
                data = await response.json()
                reply = data["choices"][0]["message"]["content"]
                return reply.strip()
        except Exception as e:
            logger.exception(f"调用DeepSeek API时发生异常: {e}")
            return "抱歉，我现在有点晕，稍后再聊吧~"
    
    async def chat_with_history(self, user_message: str, history: List[Dict[str, str]] = None) -> str:
        """
        基于历史对话生成回复。
        
        Args:
            user_message: 用户新消息
            history: 历史消息列表（可选）
        
        Returns:
            助手回复
        """
        messages = []
        # 添加系统提示
        if config.SYSTEM_PROMPT:
            messages.append({"role": "system", "content": config.SYSTEM_PROMPT})
        
        # 添加历史消息（限制长度）
        if history:
            # 只保留最近的历史记录
            for h in history[-config.MAX_HISTORY:]:
                messages.append(h)
        
        # 添加用户新消息
        messages.append({"role": "user", "content": user_message})
        
        return await self.chat(messages)

# 单例客户端
async def get_deepseek_client() -> DeepSeekClient:
    """获取DeepSeek客户端实例（异步上下文管理器）"""
    return DeepSeekClient()

if __name__ == "__main__":
    # 简单测试
    import asyncio
    async def test():
        async with DeepSeekClient() as client:
            reply = await client.chat([{"role": "user", "content": "你好，你是谁？"}])
            print(reply)
    
    asyncio.run(test())