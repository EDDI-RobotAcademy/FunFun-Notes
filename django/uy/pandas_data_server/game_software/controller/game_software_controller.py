import uuid
from django.http import JsonResponse
from django.shortcuts import render
from django.db import transaction
from django.http import JsonResponse
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from game_software.service.game_software_service_impl import GameSoftwareServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class GameSoftwareController(viewsets.ViewSet):
    gameSoftwareService = GameSoftwareServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestGameSoftwareList(self, request):
        # page, perPage 갯수를 요청 받을 수도 있어야 하니까.
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 12))
        
        paginatedGameSoftwareList, totalPages = self.gameSoftwareService.requestList(page, perPage)

        # serializer = GameSoftwareListSerializer(paginatedGameSoftwareList, many=True)

        return JsonResponse({"dataList": paginatedGameSoftwareList}, status=status.HTTP_200_OK)


# 카카오 토큰을 사용하지 않는 것은 무슨의미? =