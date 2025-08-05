from rest_framework import generics, status
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
import random
from .models import User, SMSVerification
from .serializers import UserRegisterSerializer, SMSVerificationSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        fio = serializer.validated_data['fio']


        code = str(random.randint(1000, 9999))
        SMSVerification.objects.create(email=email, code=code)

        # Отправляем письмо
        send_mail(
            subject='Код подтверждения',
            message=f'Твой код для регистрации: {code}. Он действителен 1 минуты.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email]
        )

        user, created = User.objects.get_or_create(
            email=email,
            defaults={
                'fio': fio,
                'is_active': False,
                'is_email_verified': False
            }
        )

        return Response({'detail': 'Код отправлен на email', 'code_ttl': 180}, status=status.HTTP_201_CREATED)

class VerifyEmailView(generics.GenericAPIView):
    serializer_class = SMSVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        verification = SMSVerification.objects.filter(
            email=email,
            code=code,
            is_used=False
        ).order_by('-created_at').first()


        if not verification or not verification.is_code_valid():
            return Response({'error': 'Код недействителен или истёк'}, status=status.HTTP_400_BAD_REQUEST)


        try:
            user = User.objects.get(email=email)
            user.is_active = True
            user.is_email_verified = True
            user.save()

            verification.is_used = True
            verification.save()

            # Токены
            refresh = RefreshToken.for_user(user)

            return Response({
                'detail': 'Email подтверждён',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
