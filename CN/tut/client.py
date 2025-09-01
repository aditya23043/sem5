from socket import *

#serverName = '192.168.43.139'
serverName = '192.168.44.15'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)

while True:
    message = input('Enter message (type "exit" to quit): ')
    if message.lower() == "exit":
        print("Closing connection.")
        break
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(serverAddress)
    print("Echo from server:", modifiedMessage.decode())

clientSocket.close()
