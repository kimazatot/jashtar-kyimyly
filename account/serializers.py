from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, SMSVerification


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        style={'input_type': 'password'},
        validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['fio', 'email', 'password', 'password2']
        extra_kwargs = {
            'fio': {
                'help_text': 'Минимум 3 символа кириллицей',
                'error_messages': {
                    'invalid': 'Только кириллические символы'
                }
            }
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли не совпадают"})
        return attrs

class SMSVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SMSVerification
        fields = ['email', 'code']
        extra_kwargs = {
            'code': {'help_text': '4-значный код из SMS'}
        }