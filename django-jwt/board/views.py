from pathlib import Path

import os

from django.shortcuts import render

from .models import *

# .env 파일을 읽어서 현재 환경 변수로 로드하는 패키지
from dotenv import load_dotenv

# .env 파일에 있는 값들을 os.environ 딕셔너리에 추가
load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent.parent

OIDC_OP_DOMAIN = os.getenv("OIDC_OP_DOMAIN")
OIDC_RP_CLIENT_ID = os.getenv("OIDC_RP_CLIENT_ID")
OIDC_RP_CLIENT_SECRET = os.getenv("OIDC_RP_CLIENT_SECRET")

# 브라우저에서 Keycloak 로그인 페이지로 리디렉션할 때 사용할 주소
KEYCLOAK_BROWSER_DOMAIN = os.environ.get("KEYCLOAK_BROWSER_DOMAIN")  # ex: http://localhost:8080/realms/myrealm

#  Django 서버(Docker 컨테이너)에서 Keycloak과 통신할 때 사용할 주소
KEYCLOAK_INTERNAL_DOMAIN = os.environ.get("KEYCLOAK_INTERNAL_DOMAIN")  # ex: http://keycloak:8080/realms/myrealm

# 리디렉션용 (브라우저)
OIDC_OP_AUTHORIZATION_ENDPOINT = f"{KEYCLOAK_BROWSER_DOMAIN}/protocol/openid-connect/auth"
OIDC_OP_LOGOUT_ENDPOINT = f"{KEYCLOAK_BROWSER_DOMAIN}/protocol/openid-connect/logout"

# 서버용 (Django 컨테이너 내부에서 Keycloak에 요청)
OIDC_OP_TOKEN_ENDPOINT = f"{KEYCLOAK_INTERNAL_DOMAIN}/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = f"{KEYCLOAK_INTERNAL_DOMAIN}/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = f"{KEYCLOAK_INTERNAL_DOMAIN}/protocol/openid-connect/certs"

# 메인화면
def main_view(request):
    return render(request, 'main.html')

def board_view(request):
    posts = Post.objects.all()
    return render(request, 'board.html', {'posts': posts})
