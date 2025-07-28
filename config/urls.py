
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from content.urls import router as content_router

router = routers.DefaultRouter()
router.registry.extend(content_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

]

