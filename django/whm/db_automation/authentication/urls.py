from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.controller.authentication_controller import AuthenticationController

router = DefaultRouter()
router.register(r"authentication", AuthenticationController, basename='authentication')

urlpatterns = [
    path('', include(router.urls)),
    path('logout',
         AuthenticationController.as_view({ 'post': 'requestLogout' }),
         name='로그아웃 요청'),
]