from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'Home | Bloggy',
        'posts': posts,
    }
    return render(request, 'post/index.html', context)
    #return HttpResponse("Hello World")

@login_required(login_url="/accounts/login/")
def create(request):
    if request.method == 'POST':
        form = forms.CreatePost(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.author = request.user
            f.save()
            return redirect('post:index')
    else:
        form = forms.CreatePost()
    return render(request, 'post/create.html', {'form':form})

def detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        'post':post
    }
    return render(request, 'post/details.html', context)

