from django.urls import path, include
from rest_framework.routers import DefaultRouter

from pandas_basic.controller.pandas_basic_controller import PandasBasicController

router = DefaultRouter()
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
         PandasBasicController.as_view({'get': 'requestPagenatedPandasInfo'}),
         name='Pagination이 적용된 pandas 데이터 획득'),
    path('request-statistics-summary',
         PandasBasicController.as_view({'get': 'requestPandasStatisticsSummary'}),
         name='pandas 데이터 통계 요약 획득'),
    path('request-filtered-data',
         PandasBasicController.as_view({'get': 'requestFilteredData'}),
         name='pandas 필터링 데이터 획득'),
    ]
