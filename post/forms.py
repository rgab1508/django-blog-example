from django import forms
from . import models
from pagedown.widgets import PagedownWidget

class CreatePost(forms.ModelForm):
    body = forms.CharField(widget=PagedownWidget(show_preview=False))
    class Meta:
        model = models.Post
        
        fields = ['title', 'body', 'thumbnail']

class PostAdminChangeForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'body', 'slug','thumbnail', 'author',)
        
class PostAdminCreationForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ('title', 'body', 'thumbnail','author')
        
        