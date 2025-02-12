import uuid

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from game_software.service.game_software_service_impl import GameSoftwareServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class GameSoftwareController(viewsets.ViewSet):
    gameSoftwareService = GameSoftwareServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestGameSoftwareList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedGameSoftwareList, totalPages = self.gameSoftwareService.requestList(page, perPage)

        return JsonResponse({
            "dataList": paginatedGameSoftwareList,
            "totalPages": totalPages
        }, status=status.HTTP_200_OK)

    def requestGameSoftwareCreate(self, request):
        postRequest = request.data

        gameSoftwareImage = request.FILES.get('gameSoftwareImage')
        gameSoftwareTitle = postRequest.get('gameSoftwareTitle')
        gameSoftwarePrice = postRequest.get('gameSoftwarePrice')
        gameSoftwareDescription = postRequest.get('gameSoftwareDescription')
        print(f"gameSoftwareImage: {gameSoftwareImage}, "
              f"gameSoftwareTitle: {gameSoftwareTitle}, "
              f"gameSoftwarePrice: {gameSoftwarePrice}, "
              f"gameSoftwareDescription: {gameSoftwareDescription}")

        if not all([gameSoftwareImage, gameSoftwareTitle, gameSoftwarePrice, gameSoftwareDescription]):
            return JsonResponse({"error": '모든 내용을 채워주세요!'}, status=status.HTTP_400_BAD_REQUEST)

        savedGameSoftware = self.gameSoftwareService.createGameSoftware(
            gameSoftwareTitle,
            gameSoftwarePrice,
            gameSoftwareDescription,
            gameSoftwareImage
        )

        return JsonResponse({"data": savedGameSoftware}, status=status.HTTP_200_OK)

    def requestGameSoftwareRead(self, request, pk=None):
        try:
            if not pk:
                return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)

            print(f"requestGameSoftwareRead() -> pk: {pk}")
            readGameSoftware = self.gameSoftwareService.readGameSoftware(pk)

            return JsonResponse(readGameSoftware, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

# 카카오 토큰을 사용하지 않는 것은 무슨의미? =