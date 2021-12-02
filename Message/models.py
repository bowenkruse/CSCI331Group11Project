from django.db import models
from Profile.models import *
# Create your models here.


class Message_model(models.Model):
    sender = models.ForeignKey(UserProfile, related_name='sender', on_delete=models.CASCADE)
    recipient = models.ForeignKey(UserProfile, related_name='recipient', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    body = models.CharField(max_length=1000)
    is_read = models.BooleanField(default=False)

