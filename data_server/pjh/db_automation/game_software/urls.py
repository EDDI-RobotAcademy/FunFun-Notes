from django.urls import path, include
from rest_framework.routers import DefaultRouter

from game_software.controller.game_software_controller import GameSoftwareController

router = DefaultRouter()
router.register(r"game-software", GameSoftwareController, basename='car')

urlpatterns = [
    path('', include(router.urls)),
    path('list',
         GameSoftwareController.as_view({ 'get': 'requestGameSoftwareList' }),
         name='게임 소프트웨어 항목 요청'),
    path('create',
         GameSoftwareController.as_view({ 'post': 'requestGameSoftwareCreate' }),
         name='게임 소프트웨어 등록 요청'),
]