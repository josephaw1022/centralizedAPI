from django.shortcuts import render
from rest_framework import viewsets, permissions


from .models import Article
from .serializers import ArticleSerializer


class ArticleViews(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
