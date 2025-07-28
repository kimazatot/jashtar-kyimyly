from rest_framework.routers import DefaultRouter
from .views import ActivityDirectionViewSet

router = DefaultRouter()
router.register(r'activity-directions', ActivityDirectionViewSet, basename='activitydirection')

urlpatterns = router.urls
