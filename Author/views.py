from django.shortcuts import render
import django.views.generic as generic
from django.urls import reverse_lazy

from Author.models import Author
# Create your views here.

class AuthorListView(generic.ListView):
    model = Author
    template_name = 'Author/author_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        authors = Author.objects.all().order_by('name')
        tags = []
        for a in authors:
            name_list = a.name.split()
            tag = ""
            for word in name_list:
                tag += word[0]
            tags.append(tag)
        context["tags"] = tags 
        return context
    queryset = Author.objects.all().order_by('name')
    

class AuthorDetailView(generic.DetailView):
    model = Author
    template_name = 'Author/author_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
    
class AuthorCreateView(generic.CreateView):
    model = Author
    fields = '__all__'
    template_name = 'Author/create_author.html'

class AuthorUpdateView(generic.UpdateView):
    model = Author
    fields = '__all__'
    template_name = 'Author/create_author.html'

class AuthorDeleteView(generic.DeleteView):
    model = Author
    success_url = reverse_lazy('author:author_list')
