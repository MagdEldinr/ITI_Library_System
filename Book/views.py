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

from Book.models import Book
from .serializers import BookSerializer
# Create your views here.

class BookListView(generic.ListView):
    model = Book
    template_name = 'Book/book_list.html'
    queryset = Book.objects.all().order_by('title')
    
class BookCreateView(generic.CreateView):
    model = Book
    fields = '__all__'
    template_name = 'Book/create_book.html'

class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ('publish_date', 'status', 'topic')
    template_name = 'Book/create_book.html'

class BookDeleteView(generic.DeleteView):
    model = Book
    success_url = reverse_lazy('book:book_list')


class BookAPIList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BookAPIDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
