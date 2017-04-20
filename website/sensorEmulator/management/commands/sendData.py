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
    print("Sends data values from a beddit sensor.")


    # A command must define handle()
    def handle(self, *args, **options):

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('localhost', 8000)
        sock.connect(server_address)


        while True:
            data = str(randint(0,100))
            sock.send(data.encode())
            time.sleep(1)
