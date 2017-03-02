from django.conf.urls import url, include
from . import views

app_name ='sleep'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.UserFormView.as_view(),name='register'),
    url(r'^login/$', views.ipHandling.as_view(), name='login'),
    url(r'^home/$', views.base, name='home')
]
