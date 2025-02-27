from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from image_gallery.service.image_gallery_service_impl import ImageGalleryServiceImpl


class ImageGalleryController(viewsets.ViewSet):
    imageGalleryService = ImageGalleryServiceImpl.getInstance()

    def requestImageGalleryList(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 8))
        paginatedImageGalleryList, totalItems, totalPages = self.imageGalleryService.requestList(page, perPage)

        # JSON 응답 생성
        return JsonResponse({
            "dataList": paginatedImageGalleryList,  # 게시글 정보 목록
            "totalItems": totalItems,  # 전체 게시글 수
            "totalPages": totalPages  # 전체 페이지 수
        }, status=status.HTTP_200_OK)