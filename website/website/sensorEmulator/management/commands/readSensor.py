from django.core.management import BaseCommand
import time
from random import randint
from channels import Group
#The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):
    # Show this when the user types help
    print("Simulates data values from a beddit sensor.")

    # A command must define handle()
    def handle(self, *args, **options):

        while True:
            #x = randint(0,100)
            f = open("randomdata.txt")
            for siffra in f:
                x = siffra.strip()
                Group("values").send({'text': str(siffra)})
                print("data: " + str(siffra))

                time.sleep(1)

            #Group("values").send({'text' : str(x)})
            #print("data: " + str(x))
            #time.sleep(1)
