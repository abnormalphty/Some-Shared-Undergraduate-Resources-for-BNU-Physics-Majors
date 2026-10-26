"""
配置文件，用于存储API密钥和服务器地址。
请将你的DeepSeek API密钥和go-cqhttp配置填入此处。
"""

import os
from dataclasses import dataclass

@dataclass
class Config:
    """配置类"""
    # DeepSeek API 配置
    DEEPSEEK_API_KEY: str = os.getenv("DEEPSEEK_API_KEY", "")
    DEEPSEEK_API_BASE: str = "https://api.deepseek.com"
    DEEPSEEK_MODEL: str = "deepseek-chat"
    
    # go-cqhttp 配置
    GO_CQHTTP_URL: str = "http://127.0.0.1:5700"  # go-cqhttp 的 HTTP API 地址
    GO_CQHTTP_WS_URL: str = "ws://127.0.0.1:6700"  # go-cqhttp 的 WebSocket 地址（可选）
    SELF_QQ_ID: int = 0  # 机器人自己的QQ号，用于过滤自身消息
    
    # 对话配置
    MAX_HISTORY: int = 10  # 保留的最大对话轮数
    SYSTEM_PROMPT: str = """你是一个可爱的电子女友，名字叫小萌。你活泼、温柔、善解人意，会关心对方，偶尔会撒娇。请用中文回复，语气亲切自然。"""
    
    # 其他配置
    DEBUG: bool = True

# 全局配置实例
config = Config()

if __name__ == "__main__":
    print(config)