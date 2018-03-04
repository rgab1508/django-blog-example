from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignupForm, LoginForm, ProfileEditForm
from django.views.generic import CreateView, FormView
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from post import models

# Create your views here.

# def signup_view(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             if 'next' in request.POST:
#                 return redirect(request.POST.get.next)
#             else:
#                 return redirect('post:index')
#     else:
#         form = SignupForm()
#     return render(request, 'accounts/signup.html',{'form':form})

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request, user)
#             return redirect('post:index')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'accounts/login.html', {'form':form})

def index_view(request):
    return render(request, 'accounts/accounts_index.html', {})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post:index')    

@login_required(login_url="/accounts/login/")
def profile_view(request, uid):
    user = get_object_or_404(UserProfile, uid=uid)
    user_posts = models.Post.objects.filter(author=user)
    return render(request, 'accounts/profile.html', {'user':user, 'user_posts':user_posts})

class SignupView(CreateView):
    form_class = SignupForm
    template_name = 'accounts/signup.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        else:
            form = self.form_class() 
            return render(request, self.template_name, {'form': form})

class LoginView(FormView):
    form_class = LoginForm
    template_name = 'accounts/login.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('/')
        else:
            form = self.form_class() 
            return render(request, self.template_name, {'form': form})

    
    def form_valid(self, form):
        request = self.request
        email = form.cleaned_data["email"]
        # first_name = form.cleaned_data("first_name")
        # last_name = form.cleaned_data("last_name")
        password = form.cleaned_data["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('post:index')
        return super(LoginView, self).form_invalid(form)
            
@login_required(login_url="/accounts/login/")
def profile_edit(request, uid):
    user = get_object_or_404(UserProfile, uid=uid)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, instance=user)
        print(form.errors)
        if form.is_valid():
            user.bio = request.POST['bio']
            print(form.errors)
            form.save()
            return redirect('accounts:profile', uid=user.uid)
    else:
        form = ProfileEditForm(instance=user)
    return render(request, 'accounts/profile_edit.html', {'user':user, 'form':form})