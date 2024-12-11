
from pandas_basic.repository.pandas_basic_repository_impl import PandasBasicRepositoryImpl
from pandas_basic.service.pandas_basic_service import PandasBasicService


class PandasBasicServiceImpl(PandasBasicService):

        __instance = None

        __fixedData = {
            "name": ["Alice", "Bob", "Lee", "Kim", "Jung"],
            "age" : [24,27,22,40,25]
        }

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

        def createPandasInfo(self):
            data = [
                {"name": name, "age": age}
                for name, age in zip(self.__fixedData["name"], self.__fixedData["age"])
            ]
            print(f"createPandasInfo() data: {data}")
            self.__pandasBasicRepository.createMany(data)

            return True

        def pandasInfoList(self):
            return self.__pandasBasicRepository.list()

        def paginatedPandasInfoList(self, page, perPage):
            return self.__pandasBasicRepository.pagenatedList(page, perPage)

        def statisticsSummary(self):
            return self.__pandasBasicRepository.statistics(self.__fixedData)

        def filteredPandasInfo(self, filteredDictionary):
            ormFilterDictionary = {}
            print(f"service -> filteredPandasInfo() filteredDictionary: {filteredDictionary}")

            if "name" in filteredDictionary:
                ormFilterDictionary["name__icontains"] = filteredDictionary["name"]

            if "minAge" in filteredDictionary:
                ormFilterDictionary["age__gte"] = filteredDictionary["minAge"]

            if "maxAge" in filteredDictionary:
                ormFilterDictionary["age__lte"] = filteredDictionary["maxAge"]

            print(f"service -> ormFilterDictionary: {ormFilterDictionary}")

            return self.__pandasBasicRepository.filterByCondition(**ormFilterDictionary)
                                                                # 딕셔너리 요소 분리를 위해 별 두개(**) 써줌


