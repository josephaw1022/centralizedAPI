from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .models import Message
from .serializers import MessageSerializer


class NewMessageView(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
