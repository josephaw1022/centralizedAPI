from .views import *
from django.urls import path

# urlpatterns = router.urls

urlpatterns = [
    path('message/', NewMessageView.as_view(), name="newmessage")
]
