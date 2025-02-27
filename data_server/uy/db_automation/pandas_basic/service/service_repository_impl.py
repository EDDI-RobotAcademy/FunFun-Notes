from pandas_basic.service.service_repository import PandasBasicService


class PandasBasicServiceImpl(PandasBasicService):

        __instance = None

        __fixedData = {
            "name": ["Alice", "Bob", "Lee", "Kim", "Jung"],
            "age" : [24,27,22,40,25]
        }

        def __new__(cls):
            if cls.__instance is None:
                cls.__instance = super().__new__(cls)

                cls.__instance.__pandasBasicRepository = PandasBasicServiceImpl.getInstance()

            return cls.__instance

        @classmethod
        def getInstance(cls):
            if cls.__instance is None:
                cls.__instance = cls()

            return cls.__instance


        def createPandasInfo(self):
            data = [
                {"name":name, "age":age}
                for name, age in zip(self.__fixedData["name"], self.__fixedData["age"])
            ]
            print(f"createPandasInfo() data: {data}")
            self.__pandasBasicRepository.createPandasInfo()
            return True