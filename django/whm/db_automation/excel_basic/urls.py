from django.urls import path, include
from rest_framework.routers import DefaultRouter
#DefaultRouter는 뷰셋에 대한 경로를 자동으로 생성하는 내장 DRF클래스이다

from excel_basic.controller.excel_basic_controller import ExcelBasicController
#인스턴스 생성, 등록된 뷰셋을 기반으로 DefaultRouter표준 CRUD 경로 자옫 생성

router = DefaultRouter()
router.register(r"excel-basic", ExcelBasicController, basename='excel-basic')

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-excel2db',
         ExcelBasicController.as_view({ 'get': 'requestCreateExcelInfo' }),
         name='excel 정보 데이터 생성'),
     path('request-create-info',
          ExcelBasicController.as_view({ 'get': 'requestDatabaseToExcel' }),
          name='DB 데이터를 excel로 생성'),
]