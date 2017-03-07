from django.contrib.auth.models import User
from django import forms


#register
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)


    class Meta:

        model = User
        fields  = ['username', 'email', 'password']


#ipform
class ipForm(forms.Form):
    ip_address = forms.CharField(max_length=200)
