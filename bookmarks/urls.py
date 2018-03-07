from django.conf.urls import url
from django.contrib.auth.decorators import login_required
 
from . import views
from .models import BookmarkPost #, BookmarkComment
 
app_name = 'ajax'
urlpatterns = [
    url(r'^post/(?P<pk>\d+)/bookmark/$',
        login_required(views.BookmarkView.as_view(model=BookmarkPost)),
        name='post_bookmark'),
    # url(r'^comment/(?P<pk>\d+)/bookmark/$',
    #     login_required(views.BookmarkView.as_view(model=BookmarkComment)),
    #     name='comment_bookmark'),
]