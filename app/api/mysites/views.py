from django.shortcuts import render
from .models import MySite
from .serializers import MySiteSerializer
from rest_framework.viewsets import ModelViewSet 

# Create your views here.


class MySitesViews(ModelViewSet):
    
    query_set = MySite.objects.all()
    serializer_class = MySiteSerializer
