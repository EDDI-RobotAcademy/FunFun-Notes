from abc import ABC, abstractmethod
import pandas as pd


class CarRepository(ABC):

    @abstractmethod
    def create(self, carData):
        pass

    @abstractmethod
    def findAll(self) -> pd.DataFrame:
        pass

    @abstractmethod
    def save(self, carData):
        pass
