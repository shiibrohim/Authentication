from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .models import Token

class CustomTokenAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            token_name, token_key = auth_header.split()
            if token_name != 'Token':
                raise AuthenticationFailed('Xato token')
        except ValueError:
            raise AuthenticationFailed('Xato token')

        try:
            token = Token.objects.get(key=token_key)
        except Token.DoesNotExist:
            raise AuthenticationFailed('Xato token')

        return (token.user, None)
