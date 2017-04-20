from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import ipForm
from .pleasework import start,stop,ping
from django.core.validators import validate_ipv46_address
from django.core.exceptions import ValidationError

from django.contrib.sessions.backends.db import SessionStore

#from netaddr import *

from random import randint


def base(request):
    return render(request, 'index.html')

def graph(request, id):
    print(id, "url-id")
    return render(request, 'graph.html')

class ipHandling(View):
    template_name = 'ipaddress.html'
    form_class = ipForm
    #blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        ip = request.POST["ip_address"]
        if form.is_valid():
            #validate_ipv46_address(ip)
            channel_id = str(randint(1,1000))
            start(ip, channel_id)
            #start session with id based on ip->id conversion
            #ses_id = str(int(netaddr.IPAddress(ip)))
            # s = SessionStore()
            # ses_id = str(40)
            # s['session_id'] = ses_id
            # s.create()
            #request.session['session_id'] = ses_id
            #print(ses_id, "sesid")
            return redirect('sleep:graph', id=channel_id)

        return render(request, self.template_name, {'form':form})


def stopGraph(request):
    stop()
    return redirect('/')
