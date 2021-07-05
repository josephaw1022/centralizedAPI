from rest_framework.routers import SimpleRouter
from .views import MySitesViews


router = SimpleRouter()
router.register('MySites', MySitesViews)

urlpatterns = router.urls
