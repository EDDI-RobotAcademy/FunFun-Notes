import uuid

from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from board.service.board_service_impl import BoardServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class BoardController(viewsets.ViewSet):
    boardService = BoardServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestBoardList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedBoardList, totalItems, totalPages = self.boardService.requestList(page, perPage)

        # JSON 응답 생성
        return JsonResponse({
            "dataList": paginatedBoardList,  # 게시글 정보 목록
            "totalItems": totalItems,  # 전체 게시글 수
            "totalPages": totalPages  # 전체 페이지 수
        }, status=status.HTTP_200_OK)

    def requestBoardCreate(self, request):
        postRequest = request.data

        title = postRequest.get("title")
        content = postRequest.get("content")
        userToken = postRequest.get("userToken")

        accountId = self.redisCacheService.getValueByKey(userToken)

        savedBoard = self.boardService.requestCreate(title, content, accountId)

        return JsonResponse({"data": savedBoard}, status=status.HTTP_200_OK)

    # def requestGameSoftwareRead(self, request, pk=None):
    #     try:
    #         if not pk:
    #             return JsonResponse({"error": "ID를 제공해야 합니다."}, status=400)
    #
    #         print(f"requestGameSoftwareRead() -> pk: {pk}")
    #         readGameSoftware = self.gameSoftwareService.readGameSoftware(pk)
    #
    #         return JsonResponse(readGameSoftware, status=200)
    #
    #     except Exception as e:
    #         return JsonResponse({"error": str(e)}, status=500)
