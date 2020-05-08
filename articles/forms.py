from django import forms
from . import models

class CreateArticle(forms.ModelForm):
    prepopulated_fields = {'slug':('title', )}
    class Meta:
        model = models.Article
        fields = ['title', 'slug', 'text', 'thumb']
