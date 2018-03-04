from django.contrib import admin
from django.urls import path, include
from .views import SignupView, LoginView
from . import views
app_name='accounts'

urlpatterns = [
    path('', views.index_view, name='accounts_index'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:uid>/', views.profile_view, name='profile'),
    path('profile/<str:uid>/edit', views.profile_edit, name='accounts_edit'),
    

]