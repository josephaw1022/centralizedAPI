
from .fields import MessageField
from django.contrib import admin
from .models import Message


class AdminMessage(admin.ModelAdmin):
    list_display = MessageField


admin.site.register(Message, AdminMessage)
