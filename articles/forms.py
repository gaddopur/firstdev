from django import forms
from django.contrib.admin import widgets

from . import models

class CreateArticle(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'text', 'thumb']


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.ArticleComment
        fields = ['comment',]
