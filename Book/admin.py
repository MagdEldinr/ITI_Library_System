from django.contrib import admin
from .models import Book, Topic

def make_published(modeladmin, request, queryset):
    queryset.update(status='P')
make_published.short_description = "Mark selected stories as published"

class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    ordering = ['title']
    actions = [make_published]

# Register your models here.
admin.site.register(Topic)
# admin.site.register(Book)
admin.site.register(Book, BookAdmin)