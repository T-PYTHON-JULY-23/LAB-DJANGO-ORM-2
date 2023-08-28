from django import forms
from .models import Post

class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=2048, widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4}))
    category = forms.ChoiceField(choices=Post.CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    publish_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}))
