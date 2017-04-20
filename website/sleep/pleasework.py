import time
import socket
from random import randint

'''
server_address ip should be filled in by django form and
start(), stop() should be called by start, stop button etc etc etc... Discuss...
'''

CLIENT_PORT = 10001  # Do not change this, hardcoded in the client.py file

sock = 0
server_address = 0

# Will make remote client with ip 'ip' start sending data
def start(ip, channel_id):
    global sock
    global server_address
    ip = str(ip)
    print(ip,"IPIPIPIPIPIPIPIP")

    print("uebudehudheuhduehduehu")
    print(channel_id, "channel_idPleaseWork")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (ip, CLIENT_PORT)
    sock.connect(server_address)
    sock.send(channel_id.encode())


# Will stop remote client script from running
def stop():
    data = 'stop'
    sock.send(data.encode())
    sock.close()


# Will print 'ping' on client computer
def ping():
    data = 'ping'
    sock.send(data.encode())
