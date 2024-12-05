from abc import ABC, abstractmethod
import pandas as pd

class CarRepository(ABC):
    @abstractmethod
    def fetchAll(self) -> pd.DataFrame:
        pass
