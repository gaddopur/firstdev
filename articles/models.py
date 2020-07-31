from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb = models.ImageField(upload_to='articles/images', default='articles/images/default.jfif', blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,default=None)

    def __str__(self):
        return self.title
    def snippet(self):
        return self.text[:20]+"..."

    def get_absolute_url(self):
        return reverse("articles:details", kwargs={"slug":  self.slug})

class ArticleComment(models.Model):
    comment = models.TextField()
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    child = models.ManyToManyField('self', blank=True)
    height = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  "%s" %(self.comment)
