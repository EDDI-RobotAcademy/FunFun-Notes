from xml.etree.ElementInclude import include

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#페이지네이션을 처리하기 위한 클래스 제공
#Paginator는 데이터 목록을 페이지별로 나눠, 특정 페이지에 해당하는 항목을 가져올 수 있음
#데이터 목록과 페이지크기를 입력받는다
#PageNotAnInteger는 페이지 번호가 정수 아닐때 작동
#EmptyPage는 요청된 페이지 번호가 존재하지 않거나 데이터라 없는 페이지 요청 시 작동

from pandas_basic.entity.pandas_basic_person import PandasBasicPerson
from pandas_basic.repository.pandas_basic_repository import PandasBasicRepository
import pandas as pd
#pandas 라이브러리를 가져온다
#pandas는 데이터 분석과 조작을 위한 라이브러리

class PandasBasicRepositoryImpl(PandasBasicRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createMany(self, dataList):
        pandasBasicPersonList = [
            PandasBasicPerson(name=item['name'], age=item['age'])
            for item in dataList
        ]
        #dataList에 리스트가 전달된다
        #name과 age라는 key를 가진 딕셔너리 생성


        PandasBasicPerson.objects.bulk_create(pandasBasicPersonList)

    def list(self):
        return PandasBasicPerson.objects.all()

    def pagenatedList(self, page=1, perPage=10):
        queryset = PandasBasicPerson.objects.all()
        paginator = Paginator(queryset, perPage)
        #apginator를 통해 queryset을 perpage(한 페이지에 표시할 항목 수)만큼 나누어
        # page에 입력된 수의 페이지를 가져온다
        # perpage에 입력된 수만큼 페이지에 리스트값을 넣는다
        #page=1, perpage=1이면 한페이지에 1개의 값을 넣는다
        #만약 데이터가 5개이면 <page 1 of 5>이고 1개 값만 반환

        try:
            paginatedData = paginator.page(page)


        except PageNotAnInteger:
            paginatedData = paginator.page(1)
            #예외가 발생하면 1페이지를 반환

        except EmptyPage:
            paginatedData = []
            #빈값은 없음을 표시

        return paginatedData, paginator.num_pages

    def statistics(self,targetData):
        dataFrame=pd.DataFrame(targetData)
        #DataTFrame은 2차원 표 형식의 데이터 구조로, 행과 열로 구성된 데이터 테이블
        #targetData를 DataFrame으로 표현
        describeData=dataFrame.describe(include="all").to_dict()
        #describe가 통계계산을 해준다

        return describeData

    def filterByCondition(self, **ormFilteredDictionary):
        return PandasBasicPerson.objects.filter(**ormFilteredDictionary)

