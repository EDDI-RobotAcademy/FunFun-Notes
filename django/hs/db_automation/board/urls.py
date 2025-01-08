from django.urls import path, include
from rest_framework.routers import DefaultRouter

from board.controller.board_controller import BoardController

router = DefaultRouter()
router.register(r"board", BoardController, basename='board')

urlpatterns = [
    path('', include(router.urls)),
    path('list',
         BoardController.as_view({ 'get': 'requestBoardList' }),
         name='게시판 항목 요청'),
    path('create',
         BoardController.as_view({ 'post': 'requestBoardCreate' }),
         name='게시물 등록 요청'),
    # path('read/<int:pk>',
    #      BoardController.as_view({ 'get': 'requestGameSoftwareRead' }),
    #      name='게임 소프트웨어 읽기 요청'),
]