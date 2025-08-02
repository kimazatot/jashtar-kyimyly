from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from .serializers import UserRegisterSerializer, SMSVerificationSerializer
from .models import User, SMSVerification
import random
from django.core.mail import send_mail
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from datetime import timedelta
from django.utils import timezone
from rest_framework.throttling import ScopedRateThrottle


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'register'

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']

        if cache.get(f'email_code_limit_{email}'):
            return Response(
                {'error': 'Повторите попытку через 5 минут'},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        user = serializer.save(is_active=False)
        code = str(random.randint(1000, 9999))
        SMSVerification.objects.create(email=email, code=code)
        send_mail(
            subject='Код подтверждения',
            message=f'Ваш код: {code}\nДействует 3 минуты.',
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[email],
        )

        cache.set(f'email_code_limit_{email}', True, timeout=300)

        return Response(
            {
                'detail': 'Код подтверждения отправлен',
                'email': email,
                'code_ttl': 180
            },
            status=status.HTTP_201_CREATED
        )


class VerifyEmailView(generics.GenericAPIView):
    serializer_class = SMSVerificationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        code = serializer.validated_data['code']

        try:
            verification = SMSVerification.objects.get(
                email=email,
                code=code,
                is_used=False,
                created_at__gte=timezone.now() - timedelta(minutes=3)
            )

            user = User.objects.get(email=email)
            user.is_active = True
            user.is_email_verified = True
            user.save()
            verification.is_used = True
            verification.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'detail': 'Email успешно подтвержден',
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'user_id': user.id,
                'email': user.email
            }, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(
                {'error': 'Неверный или просроченный код'},
                status=status.HTTP_400_BAD_REQUEST
            )