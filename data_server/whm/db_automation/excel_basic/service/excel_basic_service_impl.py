import os.path
#파일 경로와 관련된 작업을 쉽게 해준다
import pandas as pd
#데이터 분석 라이브러리

from excel_basic.repository.excel_basic_repository_impl import ExcelBasicRepositoryImpl
from excel_basic.service.excel_basic_service import ExcelBasicService


class ExcelBasicServiceImpl(ExcelBasicService):
    __instance = None

    __fixedExcelFile = "fixedExcelForTest.xlsx"
    #fixedExcelForTest라는 Excel파일을 넣음

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

    def __readExcel(self, excelFilePath):
        try:
            dataFrame = pd.read_excel(excelFilePath)
            #excelFilePath이라는 excel파일을 DataFrame객체로 변환

            excelDataDictionary = dataFrame.to_dict(orient='records')
            #dataFrame을 딕셔너리 형태로 변환
            #orient='records'는 각 행을 딕셔너리 형태로 변환
            #즉 Excel파일의 각 행을 하나의 딕셔너리로 변환, 그것을 리스트로 반환

            return excelDataDictionary

        #예외(e)발생 시
        except Exception as e:
            print(f"파일을 읽는 중 오류가 발생했습니다: {str(e)}")
            return []

    #Excel파일을 읽어 데이터베이스에 저장
    def createExcelToDatabase(self):
        currentWorkingDirectory = os.getcwd()
        #currentWorkingDirectory에 현재 디렉토리의 경로가 반환된다

        excelFilePath = os.path.join(currentWorkingDirectory, "resource", self.__fixedExcelFile)
        #excelFilePath에 주어진 여러 경로 요소를 하나의 경로로 결합
        #currentWorkingDirectory(현재 디렉토리의 경로),resource라는 하위 디렉토리, __fixedExcelFile에 정의된 엑셀)
        #즉 현재 디렉토리의 resource라는 하위 디렉토리내 엑셀파일을 지정

        readExcelData = self.__readExcel(excelFilePath)
        #엑셀을 읽고 그 데이터를 딕셔너리 형태로 변환

        print(f"readExcelData: {readExcelData}")

        self.__excelBasicRepository.createMany(readExcelData)
        return True

    #데이터베이스 데이터를 Excel에 저장
    def createDatabaseToExcel(self):
        currentWorkingDirectory = os.getcwd()
        generateExcelPath = os.path.join(currentWorkingDirectory, "generate", "excel_test.xlsx")
        #위와 동일한 작업진행

        excelDataList = self.__excelBasicRepository.list()
        #list라는 함수를 호출하여 값을 저장

        print(f"excelDataList: {excelDataList}")
        employeeDictionary = excelDataList.values("name", "age", "city", "score", "department")
        #필드를 추출하여 딕셔너리 형태로 반환
        #즉 필드값들을 추출하여 딕셔너리 리스트 생성

        dataFrame = pd.DataFrame(employeeDictionary)
        #DataFrame형식으로 변환하여 저장
        #DataFrame형식은 2차원 데이터 구조로,Excel의 표 형식에 적합

        dataFrame.to_excel(generateExcelPath, index=False, engine='openpyxl')
        #dataFrame을 엑셀형식으로 변환
        return True