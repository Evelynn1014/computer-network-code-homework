import random
import socket

byte = 1024
# 两个端口要保持一致
port = 8887
host = '127.0.0.1'
addr = (host, port)
import time

# 创建套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定
sock.bind(addr)
print("waiting to receive messages...")

while True:
    rand = random.randint(1, 10)
    data, addr = sock.recvfrom(byte)
    text = data.decode('utf-8')
    # 设置丢包率
    if rand < 4:
        time.sleep(0.1)
        continue
    print('The client says {!r}'.format(text))
    if text == "ping":
        #设置响应时间
        time.sleep(0.005)
        data = "pong".encode('utf-8')
        sock.sendto(data, addr)

# 关闭套接字
sock.close()
