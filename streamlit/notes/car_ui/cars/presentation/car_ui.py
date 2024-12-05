import asyncio

import streamlit as st

from cars.domain.usecase import GetCarsUseCase
from cars.infra.car_repository_impl import CarRepositoryImpl

def showCarUi():
    st.sidebar.title("Filter")
    car_repo = CarRepositoryImpl()
    usecase = GetCarsUseCase(car_repo)

    try:
        df = usecase.execute()

        st.header("전체 데이터 예시")
        st.table(df)

        select_multi = st.sidebar.multiselect("확인하고자 하는 차량 정보를 선택해주세요.", df.columns.tolist())
        start_button = st.sidebar.button("차량 정보 조회")

        if start_button:
            if select_multi:
                selected_df = df[select_multi]
                st.header("조회된 차량 정보")
                st.table(selected_df)
            else:
                st.warning("조회할 항목을 선택하세요.")

    except Exception as e:
        st.error(f"차량 데이터를 불러오지 못했습니다: {e}")
