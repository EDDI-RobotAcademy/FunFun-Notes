from abc import ABC, abstractmethod


class ExcelBasicService(ABC):
    __instance = None

    __fixedExcelFile = "fixedExcelForTest.xlsx"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__excelBasicRepository = ExcelBasicRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    @abstractmethod
    def createExcelToDatabase(self):
        pass
    