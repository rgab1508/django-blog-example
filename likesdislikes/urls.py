from django.conf.urls import url
from django.contrib.auth.decorators import login_required
 
from . import views
from .models import LikeDislike
from post.models import Post
 
app_name = 'likesdislikes'
urlpatterns = [
    url(r'^post/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
        name='post_like'),
    url(r'^post/(?P<pk>\d+)/dislike/$',
        login_required(views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
        name='post_dislike'),
    # url(r'^comment/(?P<pk>\d+)/like/$',
    #     login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
    #     name='comment_like'),
    # url(r'^comment/(?P<pk>\d+)/dislike/$',
    #     login_required(views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
    #     name='comment_dislike'),
]