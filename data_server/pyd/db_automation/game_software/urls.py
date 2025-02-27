from django.urls import path, include
from rest_framework.routers import DefaultRouter

from game_software.controller.game_software_controller import GameSoftwareController
from kakao_authentication.controller.kakao_oauth_controller import KakaoOauthController

router = DefaultRouter()
router.register(r"game-software", GameSoftwareController, basename='game-software')

urlpatterns = [
    path('', include(router.urls)),
    path('list',
         GameSoftwareController.as_view({ 'get': 'requestGameSoftware' }),
         name='Kakao Oauth 링크 요청'),
]