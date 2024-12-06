import os

from car.repository.car_repository_impl import CarRepositoryImpl
from car.service.car_service import CarService
from crawl.repository.crawl_repository_impl import CrawlRepositoryImpl

import re
import pandas as pd


class CarServiceImpl(CarService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__carRepository = CarRepositoryImpl.getInstance()
            cls.__instance.__crawlRepository = CrawlRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def cleanCarData(self, carData):
        cleanedData = []

        for car in carData:
            cleanedCar = {}

            # 각 예상 키를 정리
            for key, value in car.items():
                if isinstance(value, str):
                    # 필요 시 숫자가 아닌 문자를 제거 (예: '60 min' -> '60')
                    cleanedValue = re.sub(r'[^0-9.]', '', value)

                    # 필드 유형에 따라 추가로 정리할 수 있음
                    if key == 'power':
                        # 예: 'kW' 또는 'PS'와 같은 power 필드를 정리
                        cleaned_value = re.sub(r'[^0-9]', '', cleanedValue)
                    cleanedCar[key] = cleanedValue
                else:
                    cleanedCar[key] = value

            cleanedData.append(cleanedCar)

        return cleanedData

    def __processDriveRange(self, carData):
        # 'drive_range' 필드 처리 (예: ' km' 제거 후 float로 변환)
        if 'drive_range' in carData and isinstance(carData['drive_range'], str):
            carData['drive_range'] = float(carData['drive_range'].replace(' km', '').strip())
        return carData

    def __processEmptyFields(self, carData):
        # 빈 값 또는 유효하지 않은 값을 확인할 필드
        fields_to_check = ['전장', '전폭', '전고', '축거']

        # carData가 딕셔너리 목록일 경우 각 딕셔너리 처리
        if isinstance(carData, list):
            for car in carData:
                if isinstance(car, dict):
                    for field in fields_to_check:
                        # .get()을 사용하여 키가 없을 경우도 처리
                        field_value = car.get(field, None)

                        # 디버깅을 위한 현재 필드와 값 출력
                        print(f"Before processing field '{field}': {field_value}")

                        # 필드가 carData에 있고 유효한 값일 경우 처리
                        if field_value is None or field_value == '' or isinstance(field_value, str) and not field_value.strip():
                            # 필드가 비어 있거나 유효하지 않은 경우 기본값 할당 또는 처리
                            print(f"Field '{field}' is empty or invalid. Assigning default value or handling error.")
                            car[field] = -1
                        else:
                            # 필드가 유효한 경우 그대로 유지
                            print(f"Field '{field}' has valid data: {field_value}")
                else:
                    print(f"Unexpected data structure: {car} is not a dictionary")
        else:
            print(f"Expected carData to be a list, but got {type(carData)}")

        return carData

    def __convertRangesToNumeric(self, carData):
        # 범위 데이터를 숫자로 변환
        def parse_range(value):
            try:
                # 숫자가 아닌 문자를 제거하고 범위 분리 (예: "100-200km")
                numbers = [int(x) for x in re.findall(r'\d+', value)]
                # 범위일 경우 평균값 계산, 단일 값이면 그대로 사용
                return sum(numbers) // len(numbers) if numbers else None
            except Exception as e:
                print(f"Error parsing range: {value}, {e}")
                return None

        for car in carData:
            if 'drive_range' in car:
                car['drive_range'] = parse_range(car['drive_range'])
            if 'charge_time' in car:
                car['charge_time'] = parse_range(car['charge_time'])

        return carData

    def __convertNumericFields(self, carData):
        # 숫자 필드 변환
        def parse_numeric(value):
            try:
                return int(value)
            except ValueError:
                try:
                    return float(value)
                except ValueError:
                    print(f"Error converting value to numeric: {value}")
                    return None

        for car in carData:
            for field in ['power', '전장', '전폭', '전고', '축거']:
                if field in car:
                    car[field] = parse_numeric(car[field])
        return carData

    def crawlCarData(self):
        carData = self.__crawlRepository.crawl()
        print(f"carData: {carData}")
        cleanedCarData = self.cleanCarData(carData)
        print(f"cleanedCarData: {cleanedCarData}")
        clearKmDriveRangeData = self.__processDriveRange(cleanedCarData)
        print(f"clearKmDriveRangeData: {clearKmDriveRangeData}")
        clearDataWithEmptyFieldsProcessed = self.__processEmptyFields(clearKmDriveRangeData)
        print(f"clearDataWithEmptyFieldsProcessed: {clearDataWithEmptyFieldsProcessed}")
        numericConvertedData = self.__convertRangesToNumeric(clearDataWithEmptyFieldsProcessed)
        print(f"numericConvertedData: {numericConvertedData}")
        fullyProcessedData = self.__convertNumericFields(numericConvertedData)
        print(f"fullyProcessedData: {fullyProcessedData}")
        createdCar = self.__carRepository.createMany(numericConvertedData)


        if createdCar is not None:
            return True

        return False

    def carList(self):
        return self.__carRepository.findAll()

    def requestModifyCarText(self):
        csvFilePath = os.path.join("resource", "car_text_modify.csv")

        # 파일에서 데이터를 읽는 것은 헬퍼로 위임
        carTextList = self.__readCarTextsFromFile(csvFilePath)
        if not carTextList:
            return

        print(f"carTextList: {carTextList}")

        # 기존 데이터 가져오기
        existingCarList = self.__carRepository.findAll()
        print(f"existingCarList: {existingCarList}")

        # 기존 데이터와 파일 데이터를 기반으로 업데이트 작업만 수행
        updateCarList = self.__prepareUpdateCars(existingCarList, carTextList)
        print(f"updateCarList: {updateCarList}")

        # 업데이트 작업 실행
        if updateCarList:
            self.__updateExistingCars(updateCarList)
            return True

        print("업데이트할 데이터가 없습니다.")
        return False

    # Private Method 1: 파일에서 텍스트 읽기
    def __readCarTextsFromFile(self, csvFilePath):
        currentWorkingDirectory = os.getcwd()
        print(f"현재 작업 디렉토리: {currentWorkingDirectory}")

        # 절대 경로 생성
        absPath = os.path.join(currentWorkingDirectory, csvFilePath)
        print(f"absPath: {absPath}")

        if not os.path.exists(absPath):
            print(f"CSV 파일이 존재하지 않습니다: {absPath}")
            return None

        try:
            with open(absPath, newline="", encoding="utf-8") as csvfile:
                # 첫 번째 줄을 건너뛰고 데이터를 읽어들임
                reader = csvfile.readlines()[1:]  # 첫 번째 줄을 건너뛰고 나머지 데이터를 읽음
                return {line.strip() for line in reader if line.strip()}  # 빈 줄을 제외하고 데이터만 셋에 추가
        except Exception as e:
            print(f"CSV 파일을 읽는 중 오류 발생: {e}")
            return None

    # Private Method 2: 업데이트 데이터 준비
    def __prepareUpdateCars(self, existingCarList, carTextList):
        update_cars = []
        print(f'len(existingCarList): {len(existingCarList)}')
        print(f'len(carTextList): {len(carTextList)}')

        # carTextList가 빈 값이 아니어야 함
        if carTextList:
            # existingCarList의 각 항목에 대해 carTextList에서 값을 가져와서 넣기
            carTextList = list(carTextList)  # set이 아닌 list로 변환 (순서 보장)

            if len(existingCarList) == len(carTextList):
                for i, car in enumerate(existingCarList.to_dict("records")):
                    car['text'] = carTextList[i]  # carTextList에서 해당 인덱스의 값을 넣기
                    update_cars.append({"id": car["id"], "text": car['text']})
                    print(f"Updated car with id: {car['id']} and new text: {car['text']}")
            else:
                print("The lengths of existingCarList and carTextList do not match.")
        else:
            print("carTextList is empty.")

        return update_cars

    # Private Method 3: 기존 데이터 업데이트
    def __updateExistingCars(self, updateCarList):
        for carData in updateCarList:
            self.__carRepository.save(carData)
            print(f"업데이트된 차량 데이터: {carData['text']}")
