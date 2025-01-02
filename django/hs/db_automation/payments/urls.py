from django.db import models

# Create your models here.
from django.urls import path, include
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r"payments", PaymentsController, basename='payments')

urlpatterns = [
    path('', include(router.urls)),
    path('create',
         PaymentsController.as_view({ 'post': 'requestProcessPayments' }),
         name='결제 진행'),
]