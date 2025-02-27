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
]