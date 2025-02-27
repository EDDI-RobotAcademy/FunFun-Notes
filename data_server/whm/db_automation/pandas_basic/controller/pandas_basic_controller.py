from django.forms import model_to_dict
from django.http import JsonResponse
#JsonResponse는 JSON형식의 데이터를 응답으로 반환할때 사용
#데이터를 JSON형식으로 직렬화하여 전달
#JSON형태는 {"데이터 이름" : 값} 이다

from django.shortcuts import render
#render는 뷰함수에서 HTML 템플릿을 렌더링하고 HTTP응답을 반환
#템플릿을 렌더링하여 페이지를 반환할 때 사용

from rest_framework import viewsets, status
#REST Framework에서 API뷰를 생성하는데 사용됨
#API를 간편하게 구축할 수 있다

from rest_framework.status import HTTP_200_OK
#HTTP 200 상태 코드를 나타내며, 요청이 성공적으로 처리되었음을 의미함


from pandas_basic.serializer.pandas_info_list_serializer import PandasInfoListSerializer
from pandas_basic.service.pandas_basic_service_impl import PandasBasicServiceImpl


class PandasBasicController(viewsets.ViewSet):
    pandasBasicService = PandasBasicServiceImpl.getInstance()

    def requestCreatePandasInfo(self, request):
        isSuccess = self.pandasBasicService.createPandasInfo()
        #isSuccess에 createPandasInfo()를 생성

        return JsonResponse({"isSuccess": True}, status=status.HTTP_200_OK)
        #{"isSuccess": True}을 출력, 여기서 isSuccess는 그냥 문자임

    def requestPandasInfo(self, request):
        pandasInfoList = self.pandasBasicService.pandasInfoList()
        #리스트 생성

        serializer = PandasInfoListSerializer(pandasInfoList, many=True)
        #serializer에 serializer를 통해 JSON형식으로 변환한 데이터을 저장
        #many=True는 여러 개의 객체(리스트나 쿼리셋)를 직렬화할 때 사용하는 옵션
        #즉 리스트의 각 객체들을 직렬화하여 변환하도록 함

        return JsonResponse({"serializedPandasInfoList": serializer.data}, status=status.HTTP_200_OK)

    def requestPagenatedPandasInfo(self, request):
        getRequest = request.GET
        #URL을 통해 입력을 얻음

        page = int(getRequest.get("page", 1))
        #URL을 통해 입력이 없다면 기본적으로 1이 입력된다
        perPage = int(getRequest.get("perPage", 10))
        #URL을 통해 입력이 없다면 기본적으로 10이 입력된다

        paginatedpandasList, totalPages = self.pandasBasicService.paginatedPandasInfoList(page, perPage)
        #paginatedpandasList는 총페이지의 몇번째 페이지인지 확인,
        #totalPages에는 그 페이지의 모든 값들

        print(f"pagenatedpandasList: {paginatedpandasList}")
        print(f"pagenatedpandasList.object_list: {paginatedpandasList.object_list}")
        serializer = PandasInfoListSerializer(paginatedpandasList, many=True)
        #각 객체를 직렬화하여 변환한다

        return JsonResponse({"data": serializer.data}, status=status.HTTP_200_OK)

    def requestPandasStatisticsSummery(self,request):
        statisticsSummery=self.pandasBasicService.statisticsSummery()

        return JsonResponse({"summery":statisticsSummery},status=status.HTTP_200_OK)

    def requestFilteredData(self,request):
        getRequest = request.GET

        name = getRequest.get("name",None)
        minAge = getRequest.get("minAge", None)
        maxAge = getRequest.get("maxAge",None)

        print(f"name:{name},minAge:{minAge},maxAge:{maxAge}")

        filterDictionary={}
        if name:
            filterDictionary["name"]=name

        if minAge:
            filterDictionary["minAge"]=minAge

        if maxAge:
            filterDictionary["maxAge"]=maxAge

        # 각 요청에 값이 있으면 그 값을, 앖으면 None을 반환

        print(f"controller -> filterDictionary:{filterDictionary}")
        filteredPandasInfo = self.pandasBasicService.filteredPandasInfo(filterDictionary)

        serializer = PandasInfoListSerializer(filteredPandasInfo,many=True)

        return JsonResponse({
            "filteredData":serializer.data
        },status=status.HTTP_200_OK)




