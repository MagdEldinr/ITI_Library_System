from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
import django.views.generic as generic
from django import forms
from django.urls import reverse_lazy, reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required   
from django.contrib.auth import authenticate, login, logout

from Book.models import Book, Topic
from Author.models import Author
from .forms import UserForm, LoginForm

class HomePage(generic.TemplateView):
    template_name = 'home.html'

def search(request):
    query = request.GET.get('search')
    if query:
        book_results = Book.objects.filter(title__icontains=query)
        author_results = Author.objects.filter(name__icontains=query)
        context = {
        'book_results': book_results,
        'author_results': author_results,
        }
    template = 'results.html'
    return render(request, 'results.html', context)
   
class RegisterForm(generic.CreateView):

    model = User
    form_class = UserForm
    template_name = 'register.html'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        self.success_url = reverse('home_page')
        return super(RegisterForm, self).form_valid(form)


# class LoginForm(generic.FormView):
#     form_class = LoginForm
#     template_name = 'login.html'

#     def form_valid(self, form):
#         user = form.save(commit=False)
#         user.set_password(user.password)
#         user.save()
#         self.success_url = reverse('home_page')
#         return super(RegisterForm, self).form_valid(form)



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            per = user.get_user_permissions()
            print(per)
            return HttpResponseRedirect(reverse('home_page'))
        else:
            return HttpResponse("Invalid username or password")
    
    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('home_page'))
