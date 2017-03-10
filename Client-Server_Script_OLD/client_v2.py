'''
This script uses two web sockets.
One on port 10001 that listens for an incoming connection (from the django server to tell the script to start sending).
If incomming connection -> start socket to the incomming ip:10000 (django server) and start sending data to that ip.
Tested on both windows and manjaro
To fix:
Discuss with django team how stop should work and so on.....
Maby hardcode REMOTE_ADDR for security reasons?
'''

import time
import socket
from socket import AF_INET, SOCK_DGRAM
from random import randint

HOST = ''                # Listen on all ip's
PORT = 10001             # Arbitrary non-privileged port to listen to
REMOTE_PORT = 10000      # Remote port to send data to (django server port)

incoming_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
incoming_socket.bind((HOST, PORT))
incoming_socket.listen(5)

def main(incoming_socket):
        print('Listening...')

        #Accept incomming connection
        conn, addr = incoming_socket.accept()
        with conn:
            print('Connected by', addr)

            #Receive session id from django server
            conn.setblocking(1)
            session_id = '1'+ str(conn.recv(16).decode())
            print('Session id set to: '+  session_id)  

            #Set timeout and prevent blocking (to be able to receive data without stalling the program and waiting for it)
            conn.settimeout(10)
            conn.setblocking(0)

            #Start socket to django server and send data (same ip as incomming socket)
            REMOTE_ADDR = addr[0]
            outgoing_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server_address = (REMOTE_ADDR, REMOTE_PORT)
            outgoing_socket.connect(server_address)

            #Send session id back to django server
            outgoing_socket.send(session_id.encode())

            print('Session id sent back to django server')
            time.sleep(1)
            print('Will now start to send data to '+str(addr[0]))

            #Start loop to send data to django server
            while True:
                try:
                    #send_data = str(randint(0,100)) #Send random integer between 0-100
                    send_data = '0'+str(123)
                    outgoing_socket.send(send_data.encode())
                    time.sleep(1)

                    #Check if stop signal is received and if so, break
                    inData = conn.recv(16)
                    if(inData.decode() == 'stop'):
                        break
                    #Remove this elif l8t3R...
                    elif(inData.decode() == 'ping'):
                        print('ping')

                except socket.timeout:
                    print('Socket Timeout...')
                    break

                except BlockingIOError:
                    continue    #Is raised if no data can be received from incomming_socket (conn.recv(16))

            print('Server disconnected from you...')
            main(incoming_socket)   #Start listening for connections again...

main(incoming_socket)