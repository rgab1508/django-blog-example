from django.contrib import admin
from django.urls import path
from . import views

app_name='comments'

urlpatterns = [
    path('<int:pk>', views.comment_thread, name='thread'),
    path('<int:pk>/delete/', views.comment_delete, name='comment_delete'),    
]