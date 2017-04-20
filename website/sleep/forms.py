from django.contrib.auth.models import User
from django import forms

#ipform
class ipForm(forms.Form):
    ip_address = forms.CharField(max_length=200)
