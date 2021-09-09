from django.db import models

# Create your models here.
class TestApp(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)