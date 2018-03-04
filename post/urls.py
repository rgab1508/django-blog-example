from django.contrib import admin
from django.urls import path
from . import views

app_name='post'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<slug>/', views.pre_edit, name='pedit'),
    path('<slug:slug>/edit/', views.edit_view, name='edit'),
    path('<slug:slug>/delete/', views.post_delete, name='post_delete'),    
    path('<slug:slug>/', views.detail, name='detail'),
    # path('<slug:slug>/plz/', views.edit, name='edit'),          
]