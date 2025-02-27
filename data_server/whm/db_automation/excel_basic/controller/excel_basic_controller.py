from django.http import JsonResponse
from django.shortcuts import render
#render는 뷰함수에서 HTML 템플릿을 렌더링하고 HTTP응답을 반환
#템플릿을 렌더링하여 페이지를 반환할 때 사용
from rest_framework import viewsets, status
#REST Framework에서 API뷰를 생성하는데 사용됨
#API를 간편하게 구축할 수 있다

from excel_basic.service.excel_basic_service_impl import ExcelBasicServiceImpl


class ExcelBasicController(viewsets.ViewSet):
    excelBasicService = ExcelBasicServiceImpl.getInstance()

    def requestCreateExcelInfo(self, request):
        isSuccess = self.excelBasicService.createExcelToDatabase()
        # isSuccess에 createPandasInfo()를 생성

        return JsonResponse({"isSuccess": isSuccess}, status=status.HTTP_200_OK)
        # {"isSuccess": True}을 출력, 여기서 isSuccess는 그냥 문자임

    def requestDatabaseToExcel(self, request):
        isSuccess = self.excelBasicService.createDatabaseToExcel()

        return JsonResponse({"isSuccess": isSuccess}, status=status.HTTP_200_OK)
