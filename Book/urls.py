"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import Book.views as views

app_name = 'book'

urlpatterns = [
    path('book_list', views.BookListView.as_view(), name='book_list'),
    path('book_add', views.BookCreateView.as_view(), name='book_add'),
    path('book_edit/<int:pk>', views.BookUpdateView.as_view(), name='book_edit'),
    path('book_delete/<int:pk>', views.BookDeleteView.as_view(), name='book_delete'),
    path('api/books/', views.BookAPIList.as_view()),
    path('api/book_detail/<int:pk>/', views.BookAPIDetail.as_view()),
]
