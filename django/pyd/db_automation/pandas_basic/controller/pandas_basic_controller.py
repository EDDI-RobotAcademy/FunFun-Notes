from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from pandas_basic.service.pandas_basic_service_impl import PandasBasicServiceImpl


class PandasBasicController(viewsets.ViewSet):
    pandasBasicService = PandasBasicServiceImpl.getInstance()

    def requestCreatePandasInfo(self, request):
        isSuccess = self.pandasBasicService.createPandasInfo()

        return JsonResponse({"isSuccess": True}, status=status.HTTP_200_OK)

    def requestPandasInfo(self, request):
        pandasInfoList = self.pandasBasicService.getPandasInfo()
        serializer = PandasBasicServiceImpl
