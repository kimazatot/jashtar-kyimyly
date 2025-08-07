from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import UserProfile
from .serializers import RegisterSerializer, LoginSerializer


class RegisterViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = RegisterSerializer

    def get_queryset(self):
        return UserProfile.objects.none()

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"message": "Пользователь успешно зарегистрирован"}, status=status.HTTP_201_CREATED)


class LoginViewSet(viewsets.ViewSet):
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({"message": f"Пользователь {user.email} успешно авторизован"})
