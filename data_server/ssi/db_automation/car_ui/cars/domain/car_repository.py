from abc import ABC, abstractmethod
import pandas as pd

class CarRepository(ABC):
    @abstractmethod
    async def fetchAll(self) -> pd.DataFrame:
        pass
