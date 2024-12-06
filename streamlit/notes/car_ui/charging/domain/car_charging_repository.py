from abc import ABC, abstractmethod
import pandas as pd

class CarChargingRepository(ABC):
    @abstractmethod
    def fetchAll(self) -> pd.DataFrame:
        pass
