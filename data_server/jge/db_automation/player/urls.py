from django.urls import path, include
from rest_framework.routers import DefaultRouter

from player.controller.player_controller import PlayerController

# 웹 브라우저에서 아래 요청에 대한 기본 URL이 /dice로 시작
router = DefaultRouter()
router.register(r"player", PlayerController, basename='player')

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-player',
         PlayerController.as_view({ 'get': 'requestCreatePlayer' }),
         name='플레이어 생성'),
]