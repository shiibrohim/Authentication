from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, ProfileAPIView, ProfileUpdateAPIView, ProfileDeleteAPIView, ChangePasswordView,AuthOne, AuthTwo, send_mail_page

urlpatterns = [
    path('', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout/', LogoutAPIView.as_view()),
    path('profil/', ProfileAPIView.as_view()),
    path('profil-update/', ProfileUpdateAPIView.as_view()),
    path('profil-delete/', ProfileDeleteAPIView.as_view()),
    path('change-password/', ChangePasswordView.as_view()),
    path('auth-one/', AuthOne.as_view()),
    path('auth-two/', AuthTwo.as_view()),
    path('send-mail/', send_mail_page)
]