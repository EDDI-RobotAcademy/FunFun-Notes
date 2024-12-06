import os

import httpx
import pandas as pd
from cars.domain.car_repository import CarRepository
from httpx import AsyncClient, RequestError

from dotenv import load_dotenv
import os

load_dotenv()

base_url = os.getenv("DJANGO_URL")
print(f"DJANGO_URL: {base_url}")


class CarRepositoryImpl(CarRepository):
    __http_client = httpx.Client(
        base_url=os.getenv("DJANGO_URL"), timeout=25.0
    )

    def fetchAll(self) -> pd.DataFrame:
        try:
            endpoint = "/car/request-car-list"
            response = self.__http_client.get(endpoint)

            if response.status_code == 200:
                return pd.DataFrame(response.json())
            else:
                raise Exception(f"Failed to fetch car data: {response.status_code}")
        except RequestError as exc:
            raise Exception(f"HTTP request failed: {str(exc)}")