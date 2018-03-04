from django.contrib import admin
from .models import Post
from django.db import models
from .forms import PostAdminChangeForm, PostAdminCreationForm
from pagedown.widgets import AdminPagedownWidget
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    search_fields =['title']
    ordering = ('-pub_date',)
    list_display = ('title', 'id')
    form = PostAdminChangeForm
    add_from = PostAdminCreationForm
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget },
    }
    fieldsets = (
        (None, {'fields': ('title', 'body', 'thumbnail', 'author')}),
    )

admin.site.register(Post, PostAdmin)