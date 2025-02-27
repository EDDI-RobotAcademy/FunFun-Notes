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

            cls.__instance.__crawlRepository = CrawlRepositoryImpl.getInstance()
            cls.__instance.__carRepository = CarRepositoryImpl.getInstance()
            

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

    def modifyCarText(self):
        try:
            # CSV 파일 읽기
            csv_data = self.__load_csv('resources/car_text_modify.csv')
            if csv_data is None:
                return False

            # 데이터베이스 차량 데이터 가져오기
            car_data = self.__carRepository.findAll()
            if not car_data:
                print("No car data found in the database.")
                return False

            # 차량 데이터 수정
            modified_cars = self.__update_car_texts(car_data, csv_data)

            # 수정된 데이터 저장
            self.__save_modified_cars(modified_cars)

            print(f"Successfully modified {len(modified_cars)} cars.")
            return True

        except Exception as e:
            print(f"An error occurred while modifying car text: {e}")
            return False

    def __load_csv(self, file_path):
        try:
            return pd.read_csv(file_path)
        except Exception as e:
            print(f"Failed to read CSV file at {file_path}: {e}")
            return None

    def __update_car_texts(self, car_data, csv_data):
        modified_cars = []
        for car in car_data:
            car_id = car.get('id')
            matching_row = csv_data[csv_data['car_id'] == car_id]

            if not matching_row.empty:
                new_text = matching_row.iloc[0]['new_text']
                car['text'] = new_text
                modified_cars.append(car)

        return modified_cars

    def __save_modified_cars(self, modified_cars):
        for car in modified_cars:
            self.__carRepository.save(car)
