#!/usr/bin/env python3
import socket
import sys
import time

def run_client(server_ip, server_port, count=10, timeout=1.0):
    """
    发送 count 次 PING 消息，等待 timeout 秒接收 PONG，打印 RTT 或超时信息。
    """
    addr = (server_ip, server_port)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.settimeout(timeout)

    for seq in range(1, count+1):
        # 构造消息：包含序号和发送时间

        send_ts = time.time()#发送时间
        msg = f"{seq}号PING报文，发送时间：{send_ts}"
        try:
            sock.sendto(msg.encode('utf-8'), addr)
            data, _ = sock.recvfrom(1024)
            recv_ts = time.time()#收到回复时间

            # 计算RTT
            rtt = (recv_ts - send_ts) * 1000
            reply = data.decode('utf-8', errors='ignore').strip()
            print(f" 从{server_ip}:{server_port}收到报文，序号为{seq}，往返时延为{rtt:.3f} ms，报文信息为：“{reply}”")
        except socket.timeout:
            print(f" 序号为{seq}的报文响应超时")
    sock.sendto("exit".encode('utf-8'),addr)

        # 每次发送之间可选等待
        # time.sleep(1)

    sock.close()

if __name__ == '__main__':

    server_ip = "127.0.0.1";
    server_port = int("12000")
    run_client(server_ip, server_port)
