from django.shortcuts import render,redirect,HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, ipForm
from .pleasework import start,stop,ping
from django.core.validators import validate_ipv46_address
from django.core.exceptions import ValidationError

from django.contrib.sessions.backends.db import SessionStore

from netaddr import *

from random import randint


def base(request):
    return render(request, 'sleep/index.html')

def graph(request, id):
    print(id, "url-id")
    return render(request, 'sleep/graph.html')

#register
class UserFormView(View):
    form_class = UserForm
    template_name = 'sleep/register.html'


    #blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            #returns user objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if  user.is_active:
                    login(request, user)
                    return redirect('sleep:home')

        return render(request, self.template_name, {'form': form})

class ipHandling(View):
    template_name = 'sleep/ipaddress.html'
    form_class = ipForm
    #blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})


    def post(self, request):
        form = self.form_class(request.POST)
        ip = request.POST["ip_address"]
        if form.is_valid():
            validate_ipv46_address(ip)
            channel_id = str(23233)
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


        return render(request,self.template_name,{'form':form})


def stopGraph(request):
    stop()
    return redirect('/')
