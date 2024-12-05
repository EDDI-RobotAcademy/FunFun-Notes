from django.forms import model_to_dict
from django.shortcuts import render
from intake.container.serializer import serializers
from rest_framework import viewsets, status  #rest_framework? : API 서버를 쉽게 구축할 수 있도록 돕는 라이브러리
from rest_framework.response import Response # 라이브러리

from db_automation.dice.serializer.dice_serializer import DiceSerializer
from db_automation.dice.service.dice_service_impl import DiceServiceImpl

# Create your views here.

class DiceController(viewsets.ViewSet):
    # viewsets.ViewSet을 상속받아, DRF 기반의 API 엔드포인트를 구현

    diceService = DiceServiceImpl.getInstance()
    # Service에서 Impl을 호출, 유일한 인스턴스를 가져와서 diceService라는 변수에 저장하는 역할을 합니다.
    # diceService 객체 생성


    def requestRollDice(self, request):
        # 주사위를 굴리는 요청을 처리
        dice = self.diceService.rollDice()   #DiceServiceImpl에서 가져온 rollDice()
        # DiceServiceImpl의 rollDice() 메서드를 호출하고 결과를 반환함
        return Response(dice, status=status.HTTP_200_OK)


    def requestFindDice(self, request):
        # 특정 주사위 데이터를 조회함
        requestGetData = request.GET  # HTTP GET요청
        requestDiceId = requestGetData.get('id')
        # 위의 요청에서 id를 추출해 해당 주사위를 검색 (1)

        foundDice = self.diceService.findDice(requestDiceId)
        ## 위의 요청에서 id를 추출해 해당 주사위를 검색 (2)

        return Response(model_to_dict(foundDice), status=status.HTTP_200_OK)
        # 결과를 python 딕셔너리로 변환후 return


    def requestFindEveryDice(self, request):
        # 모든 주사위 데이터를 조회함.
        diceList = self.diceService.findEveryDice()

        serializer = DiceSerializer(diceList, many=True)
        # 주사위 데이터를 직렬화(DiceSerializer)하고 JSON 형태로 반환

        return Response(serializer.data, status=status.HTTP_200_OK)

    # 주사위 데이터 직렬화가 무슨뜻?
    # 주사위 데이터 (Dice 모델) 를 클라이언트가 이해할 수 있는 형식 (예: JSON)으로 변환하거나, 클라이언트에서 전송된 데이터를 Python객체로 변환하는 과정을 의미함

    # Django REST framework (DRF)에서 Serializer는 모델과 JSON 데이터 간의 변환을 담당하는 도구입니다.
    # 직렬화 :  Python 객체 -> JSON 또는 딕셔너리 형태로 변환