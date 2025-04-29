from rest_framework.response import Response

def custom_response(status=True, message=None, data=None, code=200):
    return Response({
        "status": status,
        "message": message,
        "data": data
    }, status=code)


MESSAGE = {
    "REGISTER_SUCCESS": "Ro‘yxatdan o‘tish muvaffaqiyatli yakunlandi",
    "LOGIN_SUCCESS": "Muvaffaqiyatli tizimga kirdingiz",
    "INVALID_CREDENTIALS": "Login yoki parol noto‘g‘ri",
    "PROFILE_UPDATED": "Profil yangilandi",
    "PASSWORD_CHANGED": "Parol muvaffaqiyatli yangilandi",
}
