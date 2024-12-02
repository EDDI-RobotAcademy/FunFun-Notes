
import pandas as pd

from cars.domain.car_repository import CarRepository


class GetCarsUseCase:
    def __init__(self, carRepository: CarRepository):
        self.carRepository = carRepository

    async def execute(self) -> pd.DataFrame:
        return await self.carRepository.fetchAll()
