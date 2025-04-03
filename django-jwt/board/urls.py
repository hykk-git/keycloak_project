from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='main'),
    path('board/', board_view, name='board'),
]