from django import forms
from tinymce.widgets import TinyMCE

from .models import Post, Comment
from marketing.models import Subscriber


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 30, 'rows': 10}))

    class Meta:
        model = Post
        fields = ['title', 'description', 'content', 'author',
                  'thumbnail', 'categories', 'featured',
                  'previous_post', 'next_post']


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))

    class Meta:
        model = Comment
        fields = ['content']
