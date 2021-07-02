

from rest_framework import routers
from .views import ArticleViews
router = routers.SimpleRouter()
router.register('article', ArticleViews, name='article')

urlpatterns = router.urls
