import socket
import time
host = '127.0.0.1'
# 两个段口必须一致
port = 8887
byte = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
# text = data.encode('utf-8')
#发送10个ping
for i in range(0,10):
    try:
        data = "ping"
        addr = (host, port)
        text = data.encode('utf-8')
        sendTime = time.time()
        sock.sendto(text, addr)
        #计数
        print(i+1)
        data, addr = sock.recvfrom(byte)
        text = data.decode("utf-8")
        #检查回复
        if text == "pong":
            backTime = time.time()
            print('The server {} replied{!r}'.format(addr, text));
            print("using time")
            print(backTime - sendTime)
#输出超时
    except: print("time out")
sock.close()
