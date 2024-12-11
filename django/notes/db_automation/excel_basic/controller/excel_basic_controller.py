from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status



class ExcelBasicController(viewsets.ViewSet):
    excelBasicService = ExcelBasicServiceImpl.getInstance()

    def requestCreateExcelInfo(self, request):
        isSuccess = self.excelBasicService.createExcelToDatabase()

        return JsonResponse({"isSuccess": isSuccess}, status=status.HTTP_200_OK)