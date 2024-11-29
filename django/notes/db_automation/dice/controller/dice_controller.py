from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from dice.service.dice_service_impl import DiceServiceImpl


# Create your views here.
class DiceController(viewsets.ViewSet):
    diceService = DiceServiceImpl.getInstance()

    def requestRollDice(self):
        dice = self.diceService.rollDice()

        return Response(dice, status=status.HTTP_200_OK)
