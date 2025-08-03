from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/', include('account.urls', namespace='account')),
    path('api/content/', include('content.urls')),
    path('api/about_direction/', include('about_direction.urls')),
]