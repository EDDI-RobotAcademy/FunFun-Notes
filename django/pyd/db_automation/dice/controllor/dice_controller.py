from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from dice.service.dice_service_impl import DiceServiceImpl


# Create your views here.

class DiceController(viewsets.ViewSet):
    diceService = DiceServiceImpl.getInstance()

    def requestRollDice(self, request):
        diceNumber = self.diceService.rollDice()

        return Response(diceNumber, status=status.HTTP_200_OK)
def requestFindDice(self, request):
    requestData = requestData.get('id')
    foundDice = self.diceService.findDice()

    return Response(foundDice, status=status.HTTP_200_OK)