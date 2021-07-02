from rest_framework import permissions, viewsets

from .models import Article
from .serializers import ArticleSerializer


class ArticleViews(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
