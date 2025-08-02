from django.contrib import admin
from django.urls import path, include
from account.views import RegisterView, VerifyEmailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('api/content/', include('content.urls')),
    path('api/about_direction/', include('about_direction.urls')),

    # пути регистрации
    path('auth/register/', RegisterView.as_view(), name='user-register'),
    path('auth/verify-email/', VerifyEmailView.as_view(), name='verify-email'),
]
