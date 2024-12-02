from django.urls import path,include
from rest_framework.routers import DefaultRouter

from dice.controllor.dice_controller import DiceController

router = DefaultRouter()
router.register(r'dice', DiceController, basename='dice')

urlpatterns = [
    path('', include(router.urls)),
    path('request-roll-dice',
         DiceController.as_view({'get': 'requestRollDice'}),
         name='주사위굴리기')
]