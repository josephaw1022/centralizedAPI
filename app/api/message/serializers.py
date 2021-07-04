from rest_framework import serializers
from .models import Message
from .fields import MessageFields


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = MessageFields
