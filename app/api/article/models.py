
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now=True)
    content = models.TextField(blank=False)
    image = models.ImageField()
    active = models.BooleanField(default=True)
