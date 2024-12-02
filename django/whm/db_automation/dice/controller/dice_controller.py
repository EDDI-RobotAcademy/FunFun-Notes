from django.forms import  model_to_dict
from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response

from dice.serializer.dice_serializer import DiceSerializer
from dice.service.dice_service_impl import DiceServiceImpl



class DiceController(viewsets.ViewSet):
    diceService=DiceServiceImpl.getInstance()

    def requestRollDice(self, request):
        dice=self.diceService.rollDice()

        return Response(dice,status=status.HTTP_200_OK)

    def requestFindDice(self,request):
        requesGetData=request.GET
        requestDiceId=requesGetData.get('id')

        foundDice=self.diceService.findDice(requestDiceId)

        return Response(
            model_to_dict(foundDice),
            status=status.HTTP_200_OK)

    def requestEveryDice(self, request):
        diceList=self.diceService.findEveryDice()
        serializer=DiceSerializer(diceList, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
