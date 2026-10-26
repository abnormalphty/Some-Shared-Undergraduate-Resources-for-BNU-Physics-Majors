#!/bin/bash

# QQ电子女友机器人启动脚本
# 使用方法: ./start.sh

set -e

cd "$(dirname "$0")"

echo "检查Python版本..."
python3 --version || { echo "Python3未安装"; exit 1; }

echo "检查依赖..."
pip3 install -r requirements.txt

echo "设置环境变量（可选）..."
if [ -f .env ]; then
    echo "加载 .env 文件"
    export $(cat .env | xargs)
else
    echo "未找到 .env 文件，请确保已设置 DEEPSEEK_API_KEY"
fi

echo "启动机器人..."
python3 main.py