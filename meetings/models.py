from email.policy import default
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


CustomUser = get_user_model()

VAR_CATEGORIES = (
    ('do', 'DSA AND OPERATING SYSTEM'),
    ('dd', 'DSA AND DATABASE'),
    ('dn', 'DSA AND NETWORKING'),
    ('od', 'OPERATING SYSTEM AND DATABASE'),
)

class Meet(models.Model):
    attendee = models.ForeignKey(CustomUser,on_delete=models.CASCADE,default=None)
    type_of_meet = models.CharField(max_length=10, choices=VAR_CATEGORIES)
    linkedin_profile = models.CharField(max_length=200, default="")
    resume_link = models.CharField(max_length=200, default="")
    accepted = models.BooleanField(default=False)
    addition_time = models.DateTimeField(auto_now_add=True)
    

    @property
    def type_of_meeting(self):
        return self.get_type_of_meet_display()