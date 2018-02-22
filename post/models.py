from django.db import models
import datetime
from django.utils import timezone
from accounts.models import UserProfile
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField()
    pub_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(UserProfile ,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title