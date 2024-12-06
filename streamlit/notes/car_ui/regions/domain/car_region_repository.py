from abc import ABC, abstractmethod
import pandas as pd

class CarRegionRepository(ABC):
    @abstractmethod
    def fetchAll(self) -> pd.DataFrame:
        pass
