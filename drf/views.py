import random

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.contrib.auth.models import User

from .models import Verification
from .serializers import RegisterSerializer, LoginSerializer, VerifySerializer, ProfileSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Ro‘yxatdan o‘tdingiz. Kod emailga yuborildi."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data)
        return Response(serializer.errors, status=400)


class ProfilView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })



class VerifyCodeView(APIView):
    def patch(self, request):
        username = request.data.get('username')
        code = request.data.get('code')
        print(code)
        try:
            user = User.objects.get(username=username)
            print(user)
            verification = Verification.objects.get(user=user)
            print(verification)
            verification.code = random.randint(1000, 9999)
            print(verification.code)
            if verification.code == code:
                user.is_active = True
                user.save()
                verification.delete()
                return Response({"message": "Malumotlar yangilandi"}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Tasdiqlash kodi noto‘g‘ri"}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({"message": "Foydalanuvchi topilmadi"}, status=status.HTTP_400_BAD_REQUEST)
        except Verification.DoesNotExist:
            return Response({"message": "Tasdiqlash kodi mavjud emas"}, status=status.HTTP_400_BAD_REQUEST)


class ProfileUpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        serializer = ProfileSerializer(request.user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)