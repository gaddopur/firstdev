from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . import models

class UserForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ('username', 'email','password1', 'password2')
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=50)
    # last_name = forms.CharField(max_length=50)
    class Meta:
        model = models.Profile
        fields = ['first_name', 'last_name', 'country','profile_pic']
