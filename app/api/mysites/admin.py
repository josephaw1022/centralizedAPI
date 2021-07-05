from django.contrib import admin
from .fields import MySiteField
from .models import MySite
# Register your models here.


class MySitesAdmin(admin.ModelAdmin):
    list_display = MySiteField


admin.site.register(MySite, MySitesAdmin)
