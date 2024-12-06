import pandas as pd

from charging.domain.car_charging_repository import CarChargingRepository


class GetChargingFeesUseCase:
    def __init__(self, carChargingRepository: CarChargingRepository):
        self.carChargingRepository = carChargingRepository

    def execute(self) -> pd.DataFrame:
        return self.carChargingRepository.fetchAll()
