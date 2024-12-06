
import pandas as pd

from cars.domain.car_repository import CarRepository


class GetCarsUseCase:
    def __init__(self, carRepository: CarRepository):
        self.carRepository = carRepository

    def execute(self) -> pd.DataFrame:
        return self.carRepository.fetchAll()
