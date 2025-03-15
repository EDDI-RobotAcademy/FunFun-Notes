from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.account_controller import AccountController

router = DefaultRouter()
router.register(r"account", AccountController, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('email',
         AccountController.as_view({ 'post': 'requestEmail' }),
         name='로그아웃 요청'),
    path('email',
         AccountController.as_view({ 'post': 'requestWithdraw' }),
         name='회원 탈퇴 요청'),
]