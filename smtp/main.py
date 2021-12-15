from socket import *
import base64

msg = "\r\n 我是内容"  # Declarations
endmsg = "\r\n.\r\n"
mailfrom = "MAIL FROM:<13846009898@163.com>\r\n"#MAIL FROM:<13846009898@163.com>
rcptto = "RCPT TO:<1371894384@qq.com>\r\n"#13846009898@163.com 1371894384@qq.com<1652872100@qq.com
data = "DATA\r\n"
quitmsg = "QUIT\r\n"
helo =  "HELO\r\n"

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = "smtp.163.com"  # Use the local Host as SMTP Server
mailPort = 25  # Specify Port For Local SMTP
connectaddress = (mailserver, mailPort)

# Create socket called clientsocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)  # Assign IP address and port number
clientSocket.connect(connectaddress)  # Connect to Local SMTP
recv = clientSocket.recv(1024)
print(recv)
if recv[:3].decode() != '220':  # Print Error Clause
    print("220 reply not received from server")

# Send HELO command and print server response.
heloCommand = "HELO Alice\r\n"
clientSocket.send(bytes(heloCommand.encode()))
recv1 = clientSocket.recv(1024)
print(recv1.decode())
if recv1.decode()[:3] != "250":
    print("250 reply not received from server.")

print('-----------------------------------')

loginini = b'AUTH LOGIN\r\n'
userCommand = (base64.b64encode(b'13846009898@163.com').decode() + '\r\n').encode()
passwordCommand = (base64.b64encode(b'XSQDJQGGWKXNXKDD').decode() + '\r\n').encode()
clientSocket.send(loginini)
recv2 = clientSocket.recv(1024).decode('utf-8')
print('222+ ', recv2)

clientSocket.send(userCommand)
recv3 = clientSocket.recv(1024).decode('utf-8')
print('333+ ', recv3)

clientSocket.send(passwordCommand)
recv4 = clientSocket.recv(1024).decode('utf-8')
print('444+ ', recv4)
print('-----------------------------------')
# Send MAIL FROM command and print server response.
clientSocket.send((mailfrom.encode()))  # send mail, had to convert to bytes
check = clientSocket.recv(1024)
print(check)  # print confirmation of working messages

# Send RCPT TO command and print server response.
clientSocket.send((rcptto.encode()))  # recieve, had to convert to bytes
check1 = clientSocket.recv(1024)
print(check1)  # print confirmation of working messages

# Send DATA command and print server response.
clientSocket.send((data.encode()))  # DATA, had to convert to bytes
check2 = clientSocket.recv(1024)
print(check2)  # print confirmation of working messages

# Message ends with a single period.
send = 'from:' + "13846009898@163.com" + '\r\n'
send += 'To:' + "1371894384@qq.com" + '\r\n'
send += 'Subject: '  +"我是主题" + '\r\n'
#send += 'Content-Type:' + 'abc' + '\t\n\r\n'
send += msg
clientSocket.sendall(((send + endmsg).encode()))  # Concatinate bits for message
check3 = clientSocket.recv(1024)
print(check3)  # print confirmation of working messages

# Send QUIT command and get server response.
clientSocket.send(bytes(quitmsg.encode()))  # Quit the session
check4 = clientSocket.recv(1024)
print(check4)
