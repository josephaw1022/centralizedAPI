"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # Rest Framework
    path('', include('rest_framework.urls')),
    # Admin
    path('admin/', admin.site.urls),
    # Frontend
    path('', include('app.client.urls')),
    # Article Module
    path('api/', include('app.api.article.urls')),
    # API Documentation
    path('api/', include_docs_urls(title="BLOG API")),
    path('api/schema', get_schema_view(
        title="Blog API",
        description="Blog API description",
    ), name="openapi-schema"),
    # Tokens
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())

]
