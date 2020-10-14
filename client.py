'''
Date: 10/13/2020
Members:
Daniel Olukiyesi - 8696093
Venkata Srikar Kovvali - 8661959
'''

import select
from client_split_messages import *
def client():

    # Retrieve Parameters passed by User
    if not(len(sys.argv) == 4):
        error_message = 'ERROR! Please enter arguments as:' +' USER_NAME  '+ 'IP_ADDRESS PORT'
        print(error_message)
        sys.exit()

    # UserName
    user_name = sys.argv[1]
    # IP Address
    IP_ADDRESS = sys.argv[2]


    try:
        # Port Number
        PORT = int(sys.argv[3])
    except Exception:
        error_message = 'ERROR! PORT NUMBER NOT A VALID INTEGER!'
        print(error_message)
        sys.exit()

    # Socket creation for the client

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Attempt connection the socket
    try:
        client_sock.connect((IP_ADDRESS, PORT))

    except BaseException:   # Print Exception if error encountered when client tries to connect to  server host/port parameters

        print(utils.CLIENT_CANNOT_CONNECT.format(IP_ADDRESS, PORT))
        sys.exit()

    sys.stdout.write(utils.CLIENT_MESSAGE_PREFIX);
    sys.stdout.flush()
    client_sock.sendall(pad_message(user_name).encode())

    while True:
        sock_collection = [sys.stdin, client_sock]

        #Create Collection Socket that are ready for input stream
        ready_for_read, ready_for_write, wait_for_error = select.select(sock_collection, [], [])

        # Iterate through readable sockets
        size = len(ready_for_read)
        pointer = 0
        while(pointer != size-1):
            sock = ready_for_read[pointer]


            if client_sock == sock:
                # Read bytes fom socket
                Data = sock.recv(utils.MESSAGE_LENGTH)
                if  Data == None:
                    print(utils.CLIENT_SERVER_DISCONNECTED.format(IP_ADDRESS, PORT))
                    sys.exit()
                else:
                    Data = Data.decode()
                    Data = Data.strip(' ')
                    sys.stdout.write(utils.CLIENT_WIPE_ME)
                    sys.stdout.write(Data)
                    sys.stdout.write(utils.CLIENT_MESSAGE_PREFIX);
                    sys.stdout.flush()
            else:
                msg = sys.stdin.readline()
                client_sock.sendall(pad_message(msg).encode())
                sys.stdout.write(utils.CLIENT_MESSAGE_PREFIX);
                sys.stdout.flush()
            pointer +=1


if __name__ == "__main__":
    sys.exit(client())
