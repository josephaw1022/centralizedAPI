from rest_framework import serializers
from .models import Message
from .fields import MessageField


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = MessageField
