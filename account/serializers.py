from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import User, SMSVerification


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [ 'fio','email', 'password', 'password2', 'is_active']

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Пользователь с таким email уже зарегистрирован")
        return value

    def validate_password(self, value):
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


class SMSVerificationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    code = serializers.CharField(max_length=4)

    class Meta:
        model = SMSVerification
        fields = ['email', 'code']
