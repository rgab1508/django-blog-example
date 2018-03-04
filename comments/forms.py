from django import forms

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput, max_length=1000)
    object_id = forms.IntegerField(widget=forms.HiddenInput)
    #parrent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea'}), max_length=500)