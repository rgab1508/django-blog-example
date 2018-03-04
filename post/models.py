from django.db import models
import datetime
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.db.models.signals import pre_save
from accounts.models import UserProfile
from comments.models import Comment
from .utils import rand_slug
from pagedown.widgets import PagedownWidget
from markdown_deux import markdown
# Create your models here.

class PostManager(models.Manager):
    pass

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    slug = models.SlugField(max_length=8,unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.jpg', blank=True)
    author = models.ForeignKey(UserProfile ,on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'slug': self.slug})

    def get_markdown(self):
        return mark_safe(markdown(self.body))

    @property
    def comments(self):
        return Comment.objects.filter_by_instance(self)

    @property
    def get_content_type(self):
        return ContentType.objects.get_for_model(self.__class__)

    objects = PostManager()


def create_slug(post, new_slug=None):
    slug = rand_slug()
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug)
    exists = qs.exists()
    if exists:
        new_slug = '{slug}{id}'.format(slug=slug, id=post.id)
        return create_slug(post, new_slug=new_slug)
    return slug

def post_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

# Execute signals pre_save
pre_save.connect(post_pre_save, sender=Post)