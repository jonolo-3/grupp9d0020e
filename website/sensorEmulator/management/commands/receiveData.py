from django.core.management import BaseCommand
import time
from random import randint
from channels import Group

from threading import Thread, Lock, active_count
import time
import socket

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    print("Simulates data values from a beddit sensor.")




    # A command must define handle()
    def handle(self, *args, **options):

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
                            print(str(addr)+':'+str(data.decode()))
                            Group("values").send({'text': str(data.decode())})
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
