from django.contrib import admin
from django.urls import path, include
from . import views

app_name='post'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<slug:slug>', views.detail, name='detail'),
]