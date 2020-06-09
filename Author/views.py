from django.shortcuts import render
import django.views.generic as generic
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework import mixins
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from Author.models import Author
from .serializers import AuthorSerializer
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


# API Section
class AuthorAPIList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class AuthorAPIDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)