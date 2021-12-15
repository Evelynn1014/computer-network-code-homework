from socket import *
import  time


# Press the green button in the gutter to run the script.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MaxBytes = 1024*1024
    # if len(sys.argv) <= 1:
    # print 'Usage : "python ProxyServer.py server_ip"\n[server_ip : It is the IP Address Of Proxy Server'
    # sys.exit(2)
    # Create a server socket, bind it to a port and start listening
    tcpSerSock = socket(AF_INET,SOCK_STREAM)
    # Fill in start.
    tcpSerSock.bind(('127.0.0.1', 8082))
    tcpSerSock.listen(5)
    tcpSerSock.settimeout(60)
    # Fill in end.
    while 1:
        # Strat receiving data from the client
        print("Ready to server...")
        tcpCliSock, addr = tcpSerSock.accept()
        print('Received a connection from:',addr)
        message = tcpCliSock.recv(MaxBytes)
        print(message)
        if len(message) <= 1:
            continue
        else:
            print(message.split()[1])
            filename = message.split()[1].partition("/".encode())[2]
            print(filename)
            fileExist = "false"
            filetouse = "/".encode() + filename
            print(filetouse)
            try:
                # Check wether the file exist in the cache
                f = open(filetouse[1:],"rb")
                outputdata = f.read()
                fileExist = "true"
                # ProxyServer finds a cache hit and generates a response message
                tcpCliSock.send(outputdata)
                print(2)
                tcpCliSock.send(("HTTP/1.0 200 OK\r\n").encode())
                tcpCliSock.send(("Content-Type:text/html\r\n").encode())

                # Fill in start.
                # Fill in end.
                print("Read from the cache")
                # Error handling for file not found in cache
            except IOError:
                if fileExist == "false":
                    # Create a socket on the proxyserver
                    c = socket(AF_INET, SOCK_STREAM)  # Fill in start. # Fill in end.
                    hostn = filename.decode().replace("www.", "", 1)
                    print(hostn)
                    try:
                        # Connect to the socket to port 80
                        # Fill in start.
                        c.connect((hostn, 80))
                        # Fill in end.
                        # Create a temporary file on this socket and ask port 80
                        # for the file requested by the client
                        c.send(("GET " + "http://" + filename.decode() + " HTTP/1.0\n\n").encode())
                        buff = c.recv(1024 * 1024)
                        #print(1)
                        #fileobj = c.makefile('rw')

                        #fileobj.write(str("GET " + "http://" + filename + " HTTP/1.0\n\n"))
                        #print(2)
                        #buff = fileobj.read(1024 * 1024)
                        # Read the response into buffer
                        # Fill in start.
                        # Fill in end.
                        # Create a new file in the cache for the requested file.
                        # Also send the response in the buffer to client socket and the corresponding file in the cache
                        print(buff.decode())
                        tmpFile = open("./" + filename.decode(), "wb")
                        # Fill in start.
                        #tmpFile = open("./" + filename.decode(), "wb")
                        # Fill in end.
                        tmpFile.write(buff)
                        tcpCliSock.send(buff)
                        tmpFile.close()
                        c.close()
                    except Exception as e:
                        c.close()
                        print(repr(e))
                        "Illegal request"
                else:
                    # HTTP response message for file not found
                    # Fill in start.
                    # Fill in end.
                    # Close the client and the server sockets
                    tcpCliSock.close()
                    # Fill in start.
                    # Fill in end.
                    # Extract the filename from the given message
