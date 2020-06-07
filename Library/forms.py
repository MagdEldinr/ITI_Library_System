from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class LoginForm(forms.Form):
    
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "password")


# class LoginForm(forms.Form):
    
#     username = forms.CharField(label='Username')
#     password = forms.CharField(widget=forms.PasswordInput())