from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField

CustomUser = get_user_model()

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.text[:20]+"..."

    def get_absolute_url(self):
        return reverse("articles:details", kwargs={"slug":  self.slug})

class ArticleComment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    child = models.ManyToManyField('self', blank=True)
    height = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  "%s" %(self.comment)
