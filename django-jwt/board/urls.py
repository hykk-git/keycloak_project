from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path("login/status/", login_status, name="login_status"),
    path("logout/", logout_view, name="logout"),
    path('board/', board_view, name='board'),
    path("login/keycloak/callback/", keycloak_callback, name="keycloak_callback"),
]