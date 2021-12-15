import socket
import time

MaxBytes = 1024*1024
host = '127.0.0.1'
port = 8083
#创立套接字
socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socket_client.settimeout(60)
socket_client.connect((host,port))
while True:
    #输入文件
    inputData = input("enter the name of file")
    #判断退出
    if inputData == "quit":
        break
    socket_client.send(inputData.encode("utf-8"))
    recvData = socket_client.recv(MaxBytes)
    print(recvData.decode())
    if not recvData:
        print("no data receved!")
        break
    recvData = socket_client.recv(MaxBytes)
    print(recvData.decode())
socket_client.close()
#退出
print("quit")
