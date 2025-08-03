from django.urls import path

from .views import RegisterView, VerifyEmailView



app_name = 'account'
urlpatterns = [

    path('register/', RegisterView.as_view(), name='user-register'),
    path('verify/', VerifyEmailView.as_view(), name='verify-email'),
]