#arbab code - need to change

import socket
import thread


class Client(object):

    def __init__(self, name, address, socket):
        self.name = name
        self.address = address
        self.socket = socket


class Channel(object):

    def __init__(self, name):
        self.name = name
        self.subscriber = []


serverName = 'localhost'
serverPort = 12000
clients = []
channels = []

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((serverName, serverPort))
server_socket.listen(5)


def checkOperation(message):
    if (message[0] == '/'):
        return True
    else:
        return False


def parseOperation(message):
    print message[1:5]
    if (message[1:5] == 'list'):
        return 'list'
    elif (message[1:5] == 'join'):
        return 'join'
    elif (message[1:7] == 'create'):
        return 'create'


def parseChannelName(message):
    Channel = message.split()[1]
    return Channel


def returnChannelList(socket):
    channelMessage = ''
    for channel in channels:
        channelMessage += channel.name + '\n'
    print channelMessage
    socket.send(channelMessage)


def createChannel(socket, channelName):
    newChannel = Channel(channelName)
    channels.append(newChannel)
    print channels


def joinChannel(socket, channelName, clientName):
    channelObj
    for channel in channels:
        if channel.name == channelName:
            channelObj = channel
    channel.subscriber.append(clientName)


def listenClient(client):
    while True:
        message = client.socket.recv(1024)
        print("CLient: " + client.name)
        print("Message: " + message)
        if checkOperation(message):
            operation = parseOperation(message)
            if (operation == 'list'):
                returnChannelList(client.socket)
            elif (operation == 'create'):
                createChannel(client.socket, parseChannelName(message))
            elif (operation == 'join'):
                joinChannel(client.socket, parseChannelName(message), client.name)
        else:
            print("Message: " + message)


while True:
    connectionSocket, addr = server_socket.accept()
    sentence = connectionSocket.recv(1024).decode()
    clientInfo = sentence.split()
    client = Client(clientInfo[0], addr, connectionSocket)
    clients.append(client)
    print('new client')
    thread.start_new_thread(listenClient, (client,))








