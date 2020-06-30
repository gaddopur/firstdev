from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    profile_pic = models.ImageField(upload_to='accounts/images', default="accounts/images/default_profile.jpg", blank=True)

    def __str__(self):
        return self.user.username
