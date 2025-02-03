from car.entity.car import Car
from car.repository.car_repository import CarRepository

import pandas as pd


class CarRepositoryImpl(CarRepository):
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
    def create(self, carData):
        car = Car(**carData)
        car.save()
        return car

    def createMany(self, carDataList):
        cars = []
        for carData in carDataList:
            car = Car(**carData)
            car.save()
            cars.append(car)
        return cars

    def findAll(self) -> pd.DataFrame:
        cars = Car.objects.all().values()
        return pd.DataFrame(cars)

    def save(self, carData):
        try:
            # 데이터베이스에서 ID로 기존 레코드 검색
            car = Car.objects.get(id=carData['id'])

            # 업데이트할 필드 설정
            car.text = carData['text']

            # 저장
            car.save()
            print(f"Car with ID {car.id} successfully updated.")
        except Car.DoesNotExist:
            print(f"Car with ID {carData['id']} does not exist in the database.")
        except Exception as e:
            print(f"An error occurred while saving the car data: {e}")
