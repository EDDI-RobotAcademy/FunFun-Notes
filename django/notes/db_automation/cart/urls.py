from django.urls import path, include
from rest_framework.routers import DefaultRouter

from cart.controller.cart_controller import CartController

router = DefaultRouter()
router.register(r"cart", CartController, basename='cart')

urlpatterns = [
    path('', include(router.urls)),
    path('create',
         CartController.as_view({ 'post': 'requestCreateCart' }),
         name='카트 생성 및 추가'),
]