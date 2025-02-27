from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from pandas_basic.entity.pandas_basic_person import PandasBasicPerson
from pandas_basic.repository.pandas_basic_repository import PandasBasicRepository
import pandas as pd

class PandasBasicRepositoryImpl(PandasBasicRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__pandasBasicRepository = PandasBasicRepositoryImpl.getInstance()
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

        PandasBasicPerson.objects.bulk_create(pandasBasicPersonList)
# objects 속성은 데이터베이스에서 CRUD(생성, 조회, 수정, 삭제) 작업을 수행할 수 있는 매니저 역할을 함
        # .bulk_create() : 다수의 레코드를 한 번의 쿼리로 삽입


    def list(self):
        return PandasBasicPerson.objects.all()



    def pagenatedList(self, page=1, perPage=10):
        # 각 10개씩 화면에 띄우기
        queryset = PandasBasicPerson.objects.all()
        paginator = Paginator(queryset, perPage)
        # Paginator(queryset: 나누고자 하는 데이터 목록, perPage: 한페이지당 표시할 항목의 수)

        try:
            paginatedData = paginator.page(page)
            # Django의 Paginator에서 특정 페이지(e.g. 1페이지, 2페이지...)의 데이터를 가져오는 코드
        except PageNotAnInteger:
            paginatedData = paginator.page(1)
        except EmptyPage:
            paginatedData = []

        return paginatedData, paginator.num_pages


    def statistics(self, targetData):
        dataFrame = pd.DataFrame(targetData)
        describeData = dataFrame.describe(include="all").to_dict()

# e.g. 아래와 같이 나타남
        # {
        #     'name': {'count': 5, 'unique': 5, 'top': 'Alice', 'freq': 1},
        #     'age': {'count': 5.0, 'mean': 30.4, 'std': 7.05, 'min': 22.0, '25%': 25.0, '50%': 30.0, '75%': 35.0, 'max': 40.0},
        # }

        return describeData


    def filterByCondition(self, **ormFilteredDictionary):
        return PandasBasicPerson.objects.filter(**ormFilteredDictionary)