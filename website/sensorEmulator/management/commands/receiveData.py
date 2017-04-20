from django.core.management import BaseCommand
import time
from random import randint
from channels import Group

from threading import Thread, Lock, active_count

import socket

from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse

#from django.contrib.sessions.backends.db import SessionStore

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    print("Simulates data values from a beddit sensor.")

    #source = str(request.session['session_id'])



    # A command must define handle()
    def handle(self, *args, **options):

        def message_handler(message_string, identifier):
            try:
                message_type = message_string[0]
                message_string = message_string[1:]
                if message_type == '0':
                    ##message_string == graph value
                    print("message received", message_string)
                    Group(identifier).send({'text': message_string})
                    #OBS message can be the empty string ""

                elif message_type == '1':
                    ##message_string == id
                    identifier = message_string

                    #for testing:
                    print("identifier set to", message_string)

                    #OBS identifier can be set to the empty string ""
                else:
                    print("unknown message_type")
            except:
                print("bad message!")

            print(identifier)
            return identifier


        def thread_client_socket(conn, addr):
            identifier = '0'
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

                            ##print(str(addr)+':'+str(data.decode()))
                            #message_handler(str(data.decode()), identifier)
                            #print(str(data.decode()))
                            #print("HEEEEEEJ")
                            identifier = message_handler(str(data.decode()), identifier)
                            #print (identifier)


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


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('', 10000)
        sock.bind(server_address)
        sock.listen(5)

        mutex_print = Lock()


        while True:
            connection, client_address = sock.accept()#stalling
            thread = Thread(target = thread_client_socket, args = (connection, client_address))
            thread.start()
            mutex_print.acquire()
            try:
                print('number of threads: '+str(active_count()))
            finally:
                mutex_print.release()
