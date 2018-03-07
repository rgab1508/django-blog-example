from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from comments.models import Comment
from likesdislikes.models import LikeDislike
from comments.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from . import forms
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-pub_date')
    q = request.GET.get('q')    
    if q:
        post_list = post_list.filter(
            Q(title__icontains=q)|
            Q(body__icontains=q)|
            Q(author__first_name__icontains=q)|
            Q(author__last_name__icontains=q)
        ).distinct()

    by = request.GET.get('by')
    if by:
        post_list = post_list.order_by(by)

    paginator = Paginator(post_list, 20) # Show 20 post per page

    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'title': 'Home | Bloggy',
        'posts': posts,
        'q':q,
        'by':by
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
            messages.add_message(request,messages.INFO,  'Post Created')
            return redirect('post:index')
            
    else:
        form = forms.CreatePost()
    return render(request, 'post/create.html', {'form':form})

def detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments #Comment.objects.filter_by_instance(post)
    initial_data = {
        'content_type':post.get_content_type,
        'object_id':post.id,
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid() and request.user.is_authenticated:
        print(comment_form.cleaned_data)
        c_type = comment_form.cleaned_data.get('content_type')
        content_type = ContentType.objects.get(model=c_type)
        obj_id = comment_form.cleaned_data.get('object_id')
        content = comment_form.cleaned_data.get('content')
        parent_comment_obj = None
        try:
            parent_comment_id = request.POST.get('parent_comment_id')
        except:
            parent_comment_id = None
        
        if parent_comment_id:
            parent_qs =Comment.objects.filter(id=parent_comment_id)
            if parent_qs.exists() and parent_qs.count() == 1:
                parent_comment_obj = parent_qs.first()

        new_comment, created = Comment.objects.get_or_create(
            user=request.user,
            content_type=content_type,
            object_id = obj_id,
            content=content,
            parent_comment=parent_comment_obj
        )
        return HttpResponseRedirect(new_comment.content_object.get_absolute_url())
    # like_obj = LikeDislike
    context = {
        'post':post,
        'comments':comments,
        'comment_form':comment_form
    }
    return render(request, 'post/details.html', context)

@login_required(login_url="/accounts/login/")
def edit_view(request, slug):
    # post = get_object_or_404(Post, slug=slug)
    # form = forms.CreatePost(request.POST or None, instance=post)

    # if form.is_valid():
    #     f = form.save(commit=False)
    #     f.save()
    #     return redirect('post:detail', slug=slug)
    # else:
    # form = forms.CreatePost(instance=post)
    return render(request, 'post/details.html')#{'form':form})
    # return HttpResponse('helllo Bitcoonnnnecttttttt')

@login_required(login_url="/accounts/login/")
def delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:list')

def edit_call(request, s):
    post = get_object_or_404(Post, slug=s)
    form = forms.CreatePost(instance=post)    
    return render(request, 'post/edit.html', {'form':form})

def pre_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = forms.CreatePost(request.POST or None, instance=post)
    return render(request, 'post/pre.html', {'form':form})

def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        if request.user != post.author:
            res = HttpResponse('No!')
            res.status_code = 403
            return res
        else:
            post.delete()
            messages.add_message(request, messages.ERROR, 'Post Deleted')
            return redirect('home')
        
    return render(request, 'post/post_delete.html', {'post':post})