from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm, LoginForm
from django.views.generic import CreateView, FormView
from django.contrib.auth.decorators import login_required

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


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('post:index')    

@login_required(login_url="/accounts/login/")
def profile_view(request):
    user = request.user
    return render(request, 'accounts/profile.html', {'user':user})

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
            
