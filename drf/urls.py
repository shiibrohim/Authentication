from django.urls import path
from .views import RegisterView, LoginView, ProfilView, ProfileUpdateView, VerifyCodeView, MySecureView

urlpatterns = [
    path('', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfilView.as_view()),
    path('update/', ProfileUpdateView.as_view()),
    path('code/', VerifyCodeView.as_view()),
    path('my-secure/', MySecureView.as_view()),
]