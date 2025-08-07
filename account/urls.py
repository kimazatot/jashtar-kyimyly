from django.urls import path
from .views import RegisterViewSet, LoginViewSet

register = RegisterViewSet.as_view({'post': 'create'})
login = LoginViewSet.as_view({'post': 'create'})

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
