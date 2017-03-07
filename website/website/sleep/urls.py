from django.conf.urls import url, include
from django.contrib import admin
from . import views

app_name ='sleep'

urlpatterns = [
    url(r'^graph/(?P<id>[0-9]+)/$', views.graph, name='graph'),
    url(r'^stop/$', views.stopGraph, name='stopGraph'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),
    #url(r'^login/$', views.ipHandling.as_view(), name='login'),
    url(r'^ip/$', views.ipHandling.as_view(), name='ip'),
    url(r'^$', views.base, name='home')
]
