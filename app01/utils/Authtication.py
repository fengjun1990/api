from rest_framework import  exceptions
from rest_framework.authentication import BaseAuthentication
from app01.models import *

class TokenAuth(BaseAuthentication):
    """token 认证类"""
    def authenticate(self, request):
        token = request.GET.get("token")
        token_obj = Token.objects.filter(token=token).first()
        if not token_obj:
            raise exceptions.AuthenticationFailed("token验证失败！")
        else:
            return token_obj.user.name,token_obj.token



