from rest_framework import serializers
from .models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
    password_repeat = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ['full_name', 'email', 'password', 'password_repeat']

    def validate_full_name(self, value):
        if len(value) < 3:
            raise serializers.ValidationError('ФИО минимум 3 символа.')
        for ch in value:
            if not (ch == ' ' or ('А' <= ch <= 'я') or ch in 'ёЁ'):
                raise serializers.ValidationError('ФИО — только русские буквы.')
        return value

    def validate_email(self, value):
        if not (value.endswith('@gmail.com') or value.endswith('@mail.ru')):
            raise serializers.ValidationError('Email должен быть example@gmail.com или example@mail.ru.')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError('Пароль минимум 8 символов.')
        if not any(ch.isdigit() for ch in value):
            raise serializers.ValidationError('Пароль должна содержать хотя бы одну цифру.')
        if not any(ch.isupper() for ch in value):
            raise serializers.ValidationError('Пароль должна содержать хотя бы одну заглавную букву.')
        return value

    def validate(self, data):
        if data['password'] != data['password_repeat']:
            raise serializers.ValidationError({'password_repeat': 'Пароли не совпадают.'})
        return data

    def create(self, validated_data):
        validated_data.pop('password_repeat')
        return UserProfile.objects.create(**validated_data)

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate_email(self, value):
        if not (value.endswith('@gmail.com') or value.endswith('@mail.ru')):
            raise serializers.ValidationError('Email должен быть example@gmail.com или example@mail.ru.')
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Пароль минимум 8 символов.")
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Пароль должна содержать хотя бы одну цифру.")
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError("Пароль должна содержать хотя бы одну заглавную букву.")
        return value

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким email не найден.")

        if user.password != password:
            raise serializers.ValidationError("Неверный пароль.")

        data['user'] = user
        return data
