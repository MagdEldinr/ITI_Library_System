from django.shortcuts import render
import django.views.generic as generic
from django.urls import reverse_lazy

from Book.models import Book
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
