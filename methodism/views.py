from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

class METHODISM(APIView):
    """
    Barcha view'lar uchun umumiy class (asosiy)
    """
    authentication_classes = []  # Authentication klasslarini kerak bo'lsa qo'shasiz
    permission_classes = [AllowAny]  # Defaultga AllowAny

    # Siz bu xususiyatni view'larda override qilishingiz mumkin
    not_auth_methods = []

    def dispatch(self, request, *args, **kwargs):
        if request.method.lower() in self.not_auth_methods:
            self.permission_classes = [AllowAny]
        return super().dispatch(request, *args, **kwargs)
