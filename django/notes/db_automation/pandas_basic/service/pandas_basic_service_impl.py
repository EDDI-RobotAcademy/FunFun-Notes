from pandas_basic.repository.pandas_basic_repository_impl import PandasBasicRepositoryImpl
from pandas_basic.service.pandas_basic_service import PandasBasicService


class PandasBasicServiceImpl(PandasBasicService):
    __instance = None

    __fixedData = {
        "name": ["Alice", "Bob", "예닮", "딩.코.재.천", "타의추종불허예닮"],
        "age": [24, 27, 22, 22, 22]
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
