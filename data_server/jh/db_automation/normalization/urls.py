from django.urls import path, include
from rest_framework.routers import DefaultRouter

from normalization.controller.normalize_controller import NormalizeController

router = DefaultRouter()
router.register(r"normalize", NormalizeController, basename='normalize')

urlpatterns = [
    path('', include(router.urls)),
    path('request-normalize',
         NormalizeController.as_view({ 'get': 'requestNormalize' }),
         name='데이터 표준화 테스트'),
]