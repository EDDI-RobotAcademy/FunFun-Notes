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
        perPage = int(getRequest.get("perPage", 12))
        paginatedGameSoftwareList, totalPages = self.gameSoftwareService.requestList(page, perPage)

        return JsonResponse({"dataList": paginatedGameSoftwareList}, status=status.HTTP_200_OK)

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
