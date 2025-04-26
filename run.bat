@echo off
REM 切换到脚本所在目录
cd /d "%~dp0"

REM 启动 server.py，并保持窗口打开
start "UDP Server" cmd /k "python server.py"

REM 等待 2 秒，不响应按键
timeout /t 2 /nobreak >nul

REM 启动 client.py，并保持窗口打开
echo 启动客户端…
start "UDP Client" cmd /k "python client.py"
