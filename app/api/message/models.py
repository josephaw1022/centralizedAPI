from django.db import models
from phone_field import PhoneField
# Create your models here.


class Message(models.Model):
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone_number = PhoneField(
        blank=True, help_text='Contact phone number')
    message = models.TextField()
    email = models.EmailField(blank=False)
