from django.db import models
from django_countries.fields import CountryField
from django.urls import reverse
# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    nationallity = CountryField()

    # class Meta:
    #     permissions = (
    #         ("add_author", "Add Author"),
    #         ("delete_author", "Delete Author"),
    #         ("edit_author", "Edit Author"),
    #     )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author:author_details", kwargs={"pk": self.pk})
    
    