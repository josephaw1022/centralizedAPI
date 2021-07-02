
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    content = models.TextField(blank=False)
    imageUrl = models.CharField(max_length=120, blank=True)
    active = models.BooleanField(default=True)
