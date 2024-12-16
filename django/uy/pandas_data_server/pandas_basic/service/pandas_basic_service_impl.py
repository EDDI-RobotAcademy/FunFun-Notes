
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
            # Django의 ORM은 SQL을 자동 생성해줌
            print(f"service -> filteredPandasInfo() filteredDictionary: {filteredDictionary}")

            if "name" in filteredDictionary:
                ormFilterDictionary["name__icontains"] = filteredDictionary["name"]
                # filteredDictionary에 'name' 키가 존재할 경우,
                # ormFilterDictionary에 'name__icontains' 조건을 추가하여, Django ORM의 부분 검색 조건을 적용하는 코드
                # name__icontains는 대소문자를 구분하지 않는 부분 일치 검색

            if "minAge" in filteredDictionary:
                ormFilterDictionary["age__gte"] = filteredDictionary["minAge"]
                # __gte: lookup 표현식
                # age__gte=20 : age가 20 이상

            if "maxAge" in filteredDictionary:
                ormFilterDictionary["age__lte"] = filteredDictionary["maxAge"]
                # age__lte=20 : age가 20 이하

            print(f"service -> ormFilterDictionary: {ormFilterDictionary}")

            return self.__pandasBasicRepository.filterByCondition(**ormFilterDictionary)
                                                                # 딕셔너리 요소 분리를 위해 별 두개(**) 써줌


