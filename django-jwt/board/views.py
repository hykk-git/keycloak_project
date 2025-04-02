from pathlib import Path

import os
import requests

from django.shortcuts import redirect, render
from django.http import JsonResponse

from rest_framework.decorators import api_view

from .models import *

# .env 파일을 읽어서 현재 환경 변수로 로드하는 패키지
from dotenv import load_dotenv

# .env 파일에 있는 값들을 os.environ 딕셔너리에 추가
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

OIDC_OP_DOMAIN = os.getenv("OIDC_OP_DOMAIN")
OIDC_RP_CLIENT_ID = os.getenv("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_RP_CLIENT_SECRET")

OIDC_OP_AUTHORIZATION_ENDPOINT = f"{OIDC_OP_DOMAIN}/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = f"{OIDC_OP_DOMAIN}/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = f"{OIDC_OP_DOMAIN}/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"{OIDC_OP_DOMAIN}/protocol/openid-connect/certs"
OIDC_OP_LOGOUT_ENDPOINT = f"{OIDC_OP_DOMAIN}/protocol/openid-connect/logout"

# 메인화면
def main_view(request):
    return render(request, 'main.html')

# httponly, secure = True로 token을 쿠키에 저장하는 함수
def set_cookies(response, access_token, refresh_token):
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        secure=False,  # 개발시에만 False
        samesite="None"
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=False, 
        samesite="None"
    )
    return response

# 쿠키를 확인해서 로그인 여부를 Boolean 타입으로 'login'으로 반환하는 함수
@api_view(['GET'])
def login_status(request):
    access_token = request.COOKIES.get('access_token')
    if access_token:
        return JsonResponse({"login": True, "message": "로그인 상태"})
    else:
        return JsonResponse({"login": False, "message": "로그아웃 상태"})

# 요청을 받고 브라우저 쿠키를 비활성화시키는 로그아웃 함수
@api_view(['POST'])
def logout_view(request):
    response = JsonResponse({"status": 200, "message": "로그아웃 되었습니다."})
    
    # 쿠키 삭제 (쿠키 유효기간 과거로 설정)
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
    return response

# 쿠키 여부를 확인하고 인가된 사용자만 보여 주는 게시판 화면
@api_view(['GET'])
def board_view(request):
    # 쿠키에서 access token 받아옴
    access_token = request.COOKIES.get("access_token")
    
    # access token 존재시 접근 허용
    if access_token:
        posts = Post.objects.all()
        return render(request, 'board.html', {'posts': posts})
    else:
        return JsonResponse({"message": "로그인이 필요합니다."}, status=401)
    
def keycloak_callback(request):
    pass