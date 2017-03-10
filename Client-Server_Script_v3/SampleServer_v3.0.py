'''
This is just a SampleServer that we used for testing purposes
while writing the client script.
This version only prints the incomming data for debugging purposes and doesn't do anything 'real' with it.
A version, similar to this, is implemented on our django server
that constantly runs in the background, listening for incoming data on port 10000
and then sends that data the the graphs by using django channels.
'''

from threading import Thread, Lock, active_count
import time
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('', 10000)
sock.bind(server_address)
sock.listen(5)

mutex_print = Lock()

def thread_client_socket(conn, addr):
    mutex_print.acquire()
    try:
        print(str(addr)+' connected')
    finally:
        mutex_print.release()
    while True:
        try:
            while True:
                data = conn.recv(16)
                mutex_print.acquire()
                try:
                    received_data = str(data.decode())
                    #print(str(addr)+':'+str(received_data)) #Uncomment to print raw data with header
                    
                    #Print to show that it's possible to check the 'header'
                    #and send the data to the apropriate destination

                    #First, get session id's by checking data header
                    if(str(received_data)[0:2] == 's1'):
                        print('Session id_1 = '+str(received_data)[1:])
                    elif(str(received_data)[0:2] == 's2'):
                        print('Session id_2 = '+str(received_data)[1:])
                    elif(str(received_data)[0:2] == 's3'):
                        print('Session id_3 = '+str(received_data)[1:])

                    #Get data for each graph, x,y,z, by checking received data header
                    elif(str(received_data)[0] == 'x'):
                        print('Graph X: = '+str(received_data)[1:])
                    elif(str(received_data)[0] == 'y'):
                        print('Graph Y: = '+str(received_data)[1:])
                    elif(str(received_data)[0] == 'z'):
                        print('Graph Z: = '+str(received_data)[1:])
 
                finally:
                    mutex_print.release()
                if not data:
                    break
        finally:
            conn.close()
            break
    mutex_print.acquire()
    try:
        print(str(addr)+' disconnected')
    finally:
        mutex_print.release()
    

while True:
    connection, client_address = sock.accept()#stalling
    thread = Thread(target = thread_client_socket, args = (connection, client_address))
    thread.start()
    mutex_print.acquire()
    try:
        print('number of threads: '+str(active_count()))
    finally:
        mutex_print.release()
