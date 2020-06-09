from django.db import models
from django.urls import reverse_lazy, reverse


from Author.models import Author
from . import fields


# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=128)
    publish_date = models.DateField()
    number_of_pages = fields.IntegerRangeField(min_value=1, max_value=5000)
    P = 'P'
    W = 'W'
    D = 'D'
    STATUS_FIELDS = (
        (P, "Published"),
        (W, "Withdrawn"),
        (D, "Draft")
    )
    status = models.CharField(choices=STATUS_FIELDS, max_length=1, default=P)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author_books')
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_books')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book:book_list")
    
    

        