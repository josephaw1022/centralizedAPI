

from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        name = "article"
        fields = ["id", "title", "content", "date", "active"]
