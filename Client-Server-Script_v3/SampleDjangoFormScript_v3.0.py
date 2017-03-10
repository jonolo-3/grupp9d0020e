import time
import socket

CLIENT_PORT = 10001 #Do not change this, hardcoded in the client.py file
server_address = 0
clientSockets = []
    
# Will make remote client with ip 'ip' start sending data
def start(ip, session_id):
    global CLIENT_PORT
    global clientSockets
    setup_flag = 1

    #Check if connection aldready have been established to ip
    for clients in clientSockets:
        if (clients[0] == ip):
            print('A connection is already established to that ip...')
            setup_flag = 0
    try:        
        if(setup_flag == 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (str(ip), CLIENT_PORT)
            sock.connect(server_address)

            #Send session id to client
            sock.send(str(session_id).encode())
            clientSockets.append((ip, sock))
    except Exception as e:
        print ('Something went wrong while creating the socket...')
    
# Will stop remote client script from running
def stop(ip):
    global server_address
    global clientSockets
    found = 0
    i = 0
    for clients in clientSockets:
        if (clients[0] == ip):
            try:
                sock = clients[1]
                data = 'stop'
                sock.send(data.encode())
                sock.close()
            except Exception as e:
                print('Something went wrong while trying to close that socket...')
                print('Client is probably down, removing socket...')
            finally:
                clientSockets.pop(i)
                found = 1
    if(found == 0):
        print('IP not found...')
    i+=1
        

# Will print 'ping' on client computer
def ping():
    global clientSockets
    data = 'ping'
    sock = clientSockets[0][1]
    sock.send(data.encode())
