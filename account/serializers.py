from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, SMSVerification


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'fio', 'password', 'password2']

    def validate_password(self, value):
        # Проверка сложности: минимум одна цифра и одна заглавная буква
        if not any(c.isdigit() for c in value) or not any(c.isupper() for c in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы одну цифру и одну заглавную букву.')
        validate_password(value)
        return value

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2': 'Пароли не совпадают'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)


class SMSVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=4)
