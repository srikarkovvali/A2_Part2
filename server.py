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
    while not False:
        ready_for_read, ready_for_error, ready_for_write = select.select(sockets,[],[])



def messaggebroadcast(server_socket, whichsock, channel, message):
    if channel is None:
        return
    for x in channels[channel]:
        if x !=server_socket and x!=whichsock:
            x.sendall(pad_message(message).encode())

if __name__ == "__main__":
    sys.exit(chatserver())