from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from intake.container.serializer import serializers
from rest_framework import viewsets, status

from pandas_basic.serializer.pandas_info_list_serializer import PandasInfoListSerializer
from pandas_basic.service.pandas_basic_service_impl import PandasBasicServiceImpl


class PandasBasicController(viewsets.ViewSet):
    pandasBasicService = PandasBasicServiceImpl.getInstance()

    def requestCreatePandasInfo(self, request):
        isSuccess = self.pandasBasicService.createPandasInfo()

        return JsonResponse({"isSuccess": isSuccess}, status=status.HTTP_200_OK)


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

        return JsonResponse({"summary":statisticsSummary}, status=status.HTTP_200_OK)

    def requestFilteredData(self, request):
        getRequest = request.GET

        name = getRequest.get("name", None)
        minAge = getRequest.get("minAge", None)
        maxAge = getRequest.get("maxAge", None)
        print(f"name: {name}, minAge: {minAge}, maxAge: {maxAge}")

        filterDictionary = {}
        if name:
            filterDictionary["name"] = name

        if minAge:
            filterDictionary["minAge"] = int(minAge)

        if maxAge:
            filterDictionary["maxAge"] = int(maxAge)

        print(f"controller -> filterDictionary: {filterDictionary}")
        filteredPandasInfo = self.pandasBasicService.filteredPandasInfo(filterDictionary)

        serializer = PandasInfoListSerializer(filteredPandasInfo, many=True)

        return JsonResponse({
            "filteredData": serializer.data
        }, status=status.HTTP_200_OK)

