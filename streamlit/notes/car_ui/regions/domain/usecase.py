import pandas as pd

from regions.domain.car_region_repository import CarRegionRepository


class GetRegionDataUseCase:
    def __init__(self, carRegionRepository: CarRegionRepository):
        self.carRegionRepository = carRegionRepository

    def execute(self) -> pd.DataFrame:
        return self.carRegionRepository.fetchAll()
