from django.db import models
# Create your models here.


class Message(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phonenumber = models.CharField(max_length=12, blank=True)
    subject = models.CharField(max_length=50, blank=True)
    message = models.TextField(blank=True)
    email = models.EmailField(blank=False)
