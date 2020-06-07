from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .forms import UserForm
# Create your views here.

class RegisterForm(generic.FormView):

    form_class = UserForm
    template_name = 'User/register.html'
    success_url = 'home.html'