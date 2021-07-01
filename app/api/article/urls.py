

from rest_framework import routers, urlpatterns
from .views import ArticleViews
router = routers.SimpleRouter()

router. register('article', ArticleViews)

urlpatterns = router.urls
