from socket import socket, AF_INET, SOCK_DGRAM

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive')

while True:
    message, clientAdlocalhostdress = serverSocket.recvfrom(2048)
    print("Client connected")
    print("Message received: " + message.decode())
    serverSocket.sendto(message, clientAdlocalhostdress)

serverSocket.close()
