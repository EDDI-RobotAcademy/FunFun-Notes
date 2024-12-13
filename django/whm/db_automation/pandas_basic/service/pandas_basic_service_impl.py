from pandas_basic.repository.pandas_basic_repository_impl import PandasBasicRepositoryImpl
from pandas_basic.service.pandas_basic_service import PandasBasicService


class PandasBasicServiceImpl(PandasBasicService):
    __instance = None

    __fixedData = {
        "name": ["Alice", "Bob", "gustj", "qudwns", "ghksals"],
        "age": [24, 27, 22, 21, 29]
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
        #name과 age를 엮어 튜플 생성
        #이후 딕션너리 리스트로 생성

        print(f"createPandasInfo() data: {data}")
        self.__pandasBasicRepository.createMany(data)
        #생성된 data를 createMany를 통해 생성

        return True
        #저장했음을 나타냄


    def pandasInfoList(self):
        return self.__pandasBasicRepository.list()
        #리스트값 반환

    def paginatedPandasInfoList(self, page, perPage):
        return self.__pandasBasicRepository.pagenatedList(page, perPage)

    def statisticsSummery(self):
        return self.__pandasBasicRepository.statistics(self.__fixedData)

    def filteredPandasInfo(self, filteredDictionary):
        ormFilterDictionary = {}
        #빈 딕셔너리 생성

        print(f"service -> filteredPandasInfo() filteredDictionary: {filteredDictionary}")

        if "name" in filteredDictionary:
            ormFilterDictionary["name__icontains"] = filteredDictionary["name"]
            #name값이 주어지면 비슷한 name를 검색한다

        if "minAge" in filteredDictionary:
            ormFilterDictionary["age__gte"] = filteredDictionary["minAge"]
            #age값이 주어지면 age이상 값을 검색한다

        if "maxAge" in filteredDictionary:
            ormFilterDictionary["age__lte"] = filteredDictionary["maxAge"]
            #age값이 주어지면 age이하 값을 검색한다

        print(f"service -> ormFilterDictionary: {ormFilterDictionary}")

        return self.__pandasBasicRepository.filterByCondition(**ormFilterDictionary)