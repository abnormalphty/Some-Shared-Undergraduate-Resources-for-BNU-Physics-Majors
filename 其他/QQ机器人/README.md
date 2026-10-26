# QQ电子女友机器人

一个基于 DeepSeek API 和 go-cqhttp 的 QQ 聊天机器人，模拟电子女友角色。

## 功能特点

- 私聊自动回复，模拟可爱女友语气
- 支持对话历史记忆（可配置轮数）
- 群聊中 @机器人 可触发回复
- 可配置系统提示词，定制角色性格
- 支持 WebSocket 和 HTTP 两种事件监听方式

## 系统架构

```
用户消息 → go-cqhttp → QQ客户端 → 消息处理器 → DeepSeek API → 生成回复 → 发送回QQ
```

## 快速开始

### 1. 环境准备

- Python 3.9+
- DeepSeek API 密钥（[申请地址](https://platform.deepseek.com/)）
- QQ小号一个（用于机器人登录）
- go-cqhttp（[下载地址](https://github.com/Mrs4s/go-cqhttp)）

### 2. 安装依赖

```bash
pip install -r requirements.txt
```

### 3. 配置 go-cqhttp

1. 下载 go-cqhttp 并解压
2. 首次运行生成配置文件 `config.yml`
3. 修改配置：
   ```yaml
   account:
     uin: 你的QQ号
     password: '你的QQ密码'
   
   message:
     post-format: array  # 建议使用array格式
   
   servers:
     - http:
         address: 127.0.0.1:5700
         timeout: 5
       ws:
         address: 127.0.0.1:6700
   ```
4. 运行 go-cqhttp，按照提示完成登录

### 4. 配置机器人

复制环境变量示例文件：

```bash
cp .env.example .env
```

编辑 `.env` 文件：

```bash
DEEPSEEK_API_KEY=你的DeepSeek API密钥
```

或直接修改 `config.py` 中的配置项：

```python
DEEPSEEK_API_KEY = "你的密钥"
SELF_QQ_ID = 你的机器人QQ号
GO_CQHTTP_URL = "http://127.0.0.1:5700"
```

### 5. 启动机器人

```bash
# 方式一：直接运行
python main.py

# 方式二：使用启动脚本
chmod +x start.sh
./start.sh
```

### 6. 开始聊天

用你的QQ号向机器人QQ号发送私聊消息，机器人会自动回复。

## 配置说明

### 主要配置文件 `config.py`

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `DEEPSEEK_API_KEY` | DeepSeek API 密钥 | 空 |
| `DEEPSEEK_API_BASE` | API 地址 | https://api.deepseek.com |
| `DEEPSEEK_MODEL` | 使用的模型 | deepseek-chat |
| `GO_CQHTTP_URL` | go-cqhttp HTTP API 地址 | http://127.0.0.1:5700 |
| `GO_CQHTTP_WS_URL` | WebSocket 地址 | ws://127.0.0.1:6700 |
| `SELF_QQ_ID` | 机器人QQ号（用于过滤自身消息） | 0 |
| `MAX_HISTORY` | 最大对话历史轮数 | 10 |
| `SYSTEM_PROMPT` | 系统提示词，定义角色性格 | 见文件 |
| `DEBUG` | 调试模式 | True |

### 自定义角色性格

修改 `config.py` 中的 `SYSTEM_PROMPT`，例如：

```python
SYSTEM_PROMPT = """你是一个傲娇的电子女友，名字叫小雪。你表面上冷淡，但实际上很关心对方。回复要简短，偶尔带点小脾气。"""
```

## 项目结构

```
.
├── config.py              # 配置文件
├── deepseek_client.py     # DeepSeek API 客户端
├── qq_client.py          # QQ 客户端（go-cqhttp 接口）
├── message_handler.py    # 消息处理器
├── main.py               # 主程序入口
├── requirements.txt      # Python 依赖
├── start.sh              # 启动脚本
├── README.md             # 说明文档
└── .env.example          # 环境变量示例
```

## 故障排除

### 1. 无法连接到 go-cqhttp

- 检查 go-cqhttp 是否正常运行
- 确认 `GO_CQHTTP_URL` 与 go-cqhttp 配置一致
- 检查防火墙是否阻止了端口访问

### 2. DeepSeek API 调用失败

- 确认 API 密钥是否正确
- 检查网络连接，确保可以访问 `api.deepseek.com`
- 查看日志中的错误信息

### 3. 机器人不回复消息

- 确认 `SELF_QQ_ID` 设置正确
- 检查 go-cqhttp 是否收到消息（查看 go-cqhttp 日志）
- 查看机器人程序日志，确认消息处理流程

### 4. 中文乱码

- 确保系统使用 UTF-8 编码
- 在启动脚本中添加 `export PYTHONUTF8=1`

## 高级功能

### 扩展群聊功能

默认只在被 @ 时回复群聊消息。如需修改，编辑 `message_handler.py` 中的 `_handle_group_msg` 方法。

### 添加命令处理

可在 `message_handler.py` 中添加命令识别逻辑，例如：

```python
if raw_message.startswith("/天气"):
    reply = await get_weather(raw_message)
```

### 持久化存储

如需将会话历史保存到数据库，可修改 `UserSession` 类，添加数据库操作。

## 注意事项

1. **遵守QQ使用条款**：使用机器人时请遵守腾讯的相关规定，避免账号风险。
2. **API调用限制**：DeepSeek API 有调用频率限制，请合理使用。
3. **隐私保护**：对话内容会发送到 DeepSeek 服务器，请勿发送敏感信息。
4. **资源消耗**：长时间运行会消耗内存，建议定期重启。

## 许可证

MIT License

## 更新日志

- 2026-03-19：初始版本发布