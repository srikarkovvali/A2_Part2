'''
Date: 10/13/2020
Members:
Daniel Olukiyesi - 8696093
Venkata Srikar Kovvali - 8661959
'''

import select
import client
from client_split_messages import *
import sys
import utils

sockets = [] #we use a list/array for the sockets
channels = {} #but we use a data dictionary for the channels because we need added functionality from them
sock_buff = 2048
sock_names = {} #names of all the sockets
partial_mess = ""

def chatserver():
    port = int(sys.argv)  #get server port from the user
    host_ip = ""
    socket_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket creation
    socket_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_s.bind((host_ip, port))
    socket_s.listen(10)

    sockets.append(socket_s) #append the socket to connections
    while 1:
        ready_for_read, ready_for_error, ready_for_write = select.select(sockets,[],[]) #list of sockets for read

        for x in ready_for_read:
            if x == socket_s:
                sockinfo, address = socket_s.accept()  #new connection
                sockets.append(sockinfo)
                isFirst = True
            else:
                curr_channel = None
                for channel in channels:
                    if x in channels[channel]:
                        curr_channel = channel
                try:
                    info = x.recv(utils.MESSAGE_LENGTH)
                    if info:

            except BaseException:
            broadcast()(server_socket, s, current_channel,
                      utils.SERVER_CLIENT_LEFT_CHANNEL.format(socket_name[s]) + "\n")
            continue


def messaggebroadcast(server_socket, whichsock, channel, message):
    if channel is None:
        return
    for x in channels[channel]:
        if x !=server_socket and x!=whichsock:
            x.sendall(pad_message(message).encode())

if __name__ == "__main__":
    sys.exit(chatserver())