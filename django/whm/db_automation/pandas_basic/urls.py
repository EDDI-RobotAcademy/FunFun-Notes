from django.urls import path, include
from rest_framework.routers import DefaultRouter
#DefaultRouter는 뷰셋에 대한 경로를 자동으로 생성하는 내장 DRF클래스이다

from pandas_basic.controller.pandas_basic_controller import PandasBasicController

router = DefaultRouter()
#인스턴스 생성, 등록된 뷰셋을 기반으로 DefaultRouter표준 CRUD 경로 자옫 생성

router.register(r"pandas-basic", PandasBasicController, basename='pandas-basic')

urlpatterns = [
    path('', include(router.urls)),
    path('request-create-info',
         PandasBasicController.as_view({ 'get': 'requestCreatePandasInfo' }),
         name='pandas 데이터 생성'),
    path('request-pandas-info',
         PandasBasicController.as_view({ 'get': 'requestPandasInfo' }),
         name='pandas 데이터 획득'),
    path('request-pagenated-pandas-info',
         PandasBasicController.as_view({ 'get': 'requestPagenatedPandasInfo' }),
         name='Pagination이 적용된 pandas 데이터 획득'),
path('request-statistics-summery',
         PandasBasicController.as_view({ 'get': 'requestPandasStatisticsSummery' }),
         name='pandas 데이터 통계요약 획득'),
]