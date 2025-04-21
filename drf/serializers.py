from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Token, Verification


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            token, created = Token.objects.get_or_create(user=user)
            return {'token': token.key}
        raise serializers.ValidationError("Noto‘g‘ri login yoki parol")


class VerifySerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField()

    def validate(self, data):
        try:
            user = User.objects.get(username=data['username'])
            verification = Verification.objects.get(user=user)

            if verification.code != data['code']:
                raise serializers.ValidationError("Tasdiqlash kodi noto‘g‘ri")

            user.is_active = True
            user.save()
            verification.delete()  # kodni olib tashlaymiz
            return {"message": "Foydalanuvchi muvaffaqiyatli faollashtirildi"}
        except User.DoesNotExist:
            raise serializers.ValidationError("Foydalanuvchi topilmadi")
        except Verification.DoesNotExist:
            raise serializers.ValidationError("Tasdiqlash kodi mavjud emas")


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)

        instance.save()
        return instance