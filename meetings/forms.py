from django import forms
from django.contrib.admin import widgets

from . import models

class CreateMeetRequest(forms.ModelForm):
    class Meta:
        model = models.Meet
        fields = ['type_of_meet', 'linkedin_profile', 'resume_link']

