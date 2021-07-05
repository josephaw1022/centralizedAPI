from django.db.models import fields
from rest_framework import serializers
from .fields import MySiteField
from .models import MySite


class MySiteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = MySiteField
        model = MySite
