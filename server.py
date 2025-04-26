import socket
import random

def run_server(host='0.0.0.0', port=12000):
    """
    启动一个简单的 UDP 回显服务器。
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    print(f"[*] UDP server开始监听，地址为{host}:{port}")

    try:
        while True:
            data, addr = sock.recvfrom(1024)  # 接收数据报文
            text = data.decode('utf-8', errors='ignore')  # 解码数据为字符串
            if random.random() < 0.8:
                print(f"从{addr[0]}:{addr[1]}接收报文：{text.strip()}")  # 打印接收到的内容
                # 将收到的数据原样返回，注意编码成 UTF-8 字节流
                sock.sendto(f"pong:{text}".encode('utf-8'), addr)
                print(f"发送至{addr[0]}:{addr[1]} 报文信息：{text.strip()}")
            else:
                print(f"模拟数据丢失")
            if text=="exit" :
                print("\n[!] Server关闭")
                break
    except KeyboardInterrupt:
        print("\n[!] Server关闭")
    finally:
        sock.close()

if __name__ == '__main__':
    run_server()
