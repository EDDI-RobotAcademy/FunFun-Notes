from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from pandas_basic.serializer.pandas_info_list_serializer import PandasInfoListSerializer
from pandas_basic.service.pandas_basic_service_impl import PandasBasicServiceImpl


class PandasBasicController(viewsets.ViewSet):
    pandasBasicService = PandasBasicServiceImpl.getInstance()

    def requestCreatePandasInfo(self, request):
        isSuccess = self.pandasBasicService.createPandasInfo()

        return JsonResponse({"isSuccess": True}, status=status.HTTP_200_OK)

    def requestPandasInfo(self, request):
        pandasInfoList = self.pandasBasicService.pandasInfoList()
        serializer = PandasInfoListSerializer(pandasInfoList, many=True)

        return JsonResponse({"serializedPandasInfoList": serializer.data}, status=status.HTTP_200_OK)

    def requestPagenatedPandasInfo(self, request):
        getRequest = request.GET
        page = int(getRequest.get("page", 1))
        perPage = int(getRequest.get("perPage", 10))

        paginatedpandasList, totalPages = self.pandasBasicService.paginatedPandasInfoList(page, perPage)
        print(f"paginatedpandasList: {paginatedpandasList}")
        print(f"paginatedpandasList.object_list: {paginatedpandasList.object_list}")
        serializer = PandasInfoListSerializer(paginatedpandasList, many=True)

        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    def requestPandasStatisticsSummary(self, request):
        statisticsSummary = self.pandasBasicService.statisticsSummary()

        return JsonResponse({"summary": statisticsSummary}, status=status.HTTP_200_OK)
