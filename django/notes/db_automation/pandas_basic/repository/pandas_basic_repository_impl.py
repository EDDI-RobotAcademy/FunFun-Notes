from pandas_basic.entity.pandas_basic_person import PandasBasicPerson
from pandas_basic.repository.pandas_basic_repository import PandasBasicRepository


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
    