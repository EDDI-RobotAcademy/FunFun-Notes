from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from pandas_basic.entity.pandas_basic_person import PandasBasicPerson
from pandas_basic.repository.pandas_basic_repository import PandasBasicRepository

import pandas as pd


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

        PandasBasicPerson.objects.bulk_create(pandasBasicPersonList)

    def list(self):
        return PandasBasicPerson.objects.all()

    def pagenatedList(self, page=1, perPage=10):
        queryset = PandasBasicPerson.objects.all()
        paginator = Paginator(queryset, perPage)

        try:
            paginatedData = paginator.page(page)
        except PageNotAnInteger:
            paginatedData = paginator.page(1)
        except EmptyPage:
            paginatedData = []

        return paginatedData, paginator.num_pages

    def statistics(self, targetData):
        dataFrame = pd.DataFrame(targetData)
        describeData = dataFrame.describe(include="all").to_dict()

        return describeData

    def filterByCondition(self, **ormFilteredDictionary):
        return PandasBasicPerson.objects.filter(**ormFilteredDictionary)
