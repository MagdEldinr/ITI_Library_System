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

import Author.views as views

app_name = 'author'

urlpatterns = [
    path('author_details/<int:pk>', views.AuthorDetailView.as_view(), name='author_details'),
    path('author_list', views.AuthorListView.as_view(), name='author_list'),
    path('author_add', views.AuthorCreateView.as_view(), name='author_add'),
    path('author_edit/<int:pk>', views.AuthorUpdateView.as_view(), name='author_edit'),
    path('author_delete/<int:pk>', views.AuthorDeleteView.as_view(), name='author_delete'),
    path('api/authors/', views.AuthorAPIList.as_view()),
    path('api/author_detail/<int:pk>/', views.AuthorAPIDetail.as_view()),
]
