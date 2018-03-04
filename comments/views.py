from django.shortcuts import render, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.http import Http404, HttpResponseRedirect, HttpResponse
from .models import Comment
from .forms import CommentForm

# Create your views here.
def comment_delete(request, pk):
    try:
        c = Comment.objects.get(id=pk)
    except:
        raise Http404

    if c.user != request.user:
        response = HttpResponse("NO!")
        response.status_code = 403
        return response
    
    if request.method == 'POST':
        post_url = c.content_object.get_absolute_url()
        c.delete()
        return HttpResponseRedirect(post_url)
    context = {
        'c':c
    }
    return render(request, 'comments/confirm_delete.html', context)

def comment_thread(request, pk):
    try:
        c = Comment.objects.get(id=pk)
    except:
        raise Http404

    if not c.is_parent:
        c = c.parent_comment

    initial_data = {
        'content_type':c.content_object.get_content_type,
        'object_id':c.object_id,
    }
    print(initial_data)
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if comment_form.is_valid():
        print(comment_form.errors)
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
    context = {
        'c':c,
        'comment_form':comment_form
    }
    
    return render(request, 'comments/comment_thread.html', context)