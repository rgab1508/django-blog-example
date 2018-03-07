from django.db import models
from accounts.models import UserProfile
from post.models import Post
# Create your models here.
class BookmarkBase(models.Model):
    class Meta:
        abstract = True
 
    user = models.ForeignKey(UserProfile, verbose_name="User", on_delete=models.CASCADE)
 
    def __str__(self):
        return self.user.first_name

class BookmarkPost(BookmarkBase):
    class Meta:
        db_table = "bookmark_post"
 
    obj = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
 
 
# class BookmarkComment(BookmarkBase):
#     class Meta:
#         db_table = "bookmark_comment"
 
#     obj = models.ForeignKey(Comment, verbose_name="Comment")