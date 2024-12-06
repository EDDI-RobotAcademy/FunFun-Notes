import asyncio

import streamlit as st

from cars.domain.usecase import GetCarsUseCase
from cars.infra.car_repository_impl import CarRepositoryImpl

def showCarUi():
    car_repo = CarRepositoryImpl()
    usecase = GetCarsUseCase(car_repo)

    try:
        df = usecase.execute()

        st.header("전체 데이터 예시")
        st.table(df)

    except Exception as e:
        st.error(f"차량 데이터를 불러오지 못했습니다: {e}")
