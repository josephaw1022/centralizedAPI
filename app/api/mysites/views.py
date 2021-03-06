from django.shortcuts import render
from .models import MySite
from .serializers import MySiteSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class MySitesViews(ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = MySite.objects.all()
    serializer_class = MySiteSerializer
