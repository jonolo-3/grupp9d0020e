from django.core.management import BaseCommand
import time
from random import randint
from channels import Group

from threading import Thread, Lock, active_count

import socket

from django.http import HttpResponse
from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse

from django.contrib.sessions.backends.db import SessionStore

#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    print("Simulates data values from a beddit sensor.")




    # A command must define handle()
    def handle(self, *args, **options):

        #while True:

            # print("RECIEVEEEEEEEEEEEEEEEEEEEEEEEE")
            #
            # #source = str(request.session['session_id'])
            # source = str(37)
            # #print("source:",source, " ", "value:", str(data.decode()))
            #
            # #print(str(addr)+':'+str(data.decode()))
            # #Group(source).send({'text': str(data.decode())})
            # data = 344
            # Group(source).send({'text': str(data)})
            #
            # #print(str(addr)+':'+str(data.decode()))
            # #Group("values").send({'text': str(data.decode())})
            # time.sleep(1)


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

                            #print("RECIEVEEEEEEEEEEEEEEEEEEEEEEEE")
                            #source = str(request.session['session_id'])
                            #print("source:",source, " ", "value:", str(data.decode()))

                            # print(str(addr)+':'+str(data.decode()))
                            #Group(source).send({'text': str(data.decode())})
                            #print(str(addr)+':'+str(data.decode()))
                            #Group("values").send({'text': str(data.decode())})

                            print("RECIEVEEEEEEEEEEEEEEEEEEEEEEEE")
                            #
                            #global request
                            # if 'session_id' in request.session:
                            #     print("dejidjeijd")
                            #     source = str(request.session['session_id'])
                            print(str(addr), "ADDRESSSSS")
                            source = str(37)
                            # #print("source:",source, " ", "value:", str(data.decode()))
                            #
                            # #print(str(addr)+':'+str(data.decode()))
                            # Group(source).send({'text': str(data.decode())})
                            data = 344
                            Group(source).send({'text': str(data)})
                            #
                            # #print(str(addr)+':'+str(data.decode()))
                            # #Group("values").send({'text': str(data.decode())})
                            # time.sleep(1)

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
