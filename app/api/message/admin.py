
from .fields import MessageFields
from django.contrib import admin
from .models import Message
from .fields import MessageFields


class AdminMessage(admin.ModelAdmin):
    list_display = MessageFields


admin.site.register(Message, AdminMessage)
