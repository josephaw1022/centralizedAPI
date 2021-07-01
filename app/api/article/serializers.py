

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        name = 'Article'
        fields = ['id', 'title', 'content', 'image', 'date', 'active']
