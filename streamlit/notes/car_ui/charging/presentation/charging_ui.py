import streamlit as st

from charging.domain.usecase import GetChargingFeesUseCase
from charging.infra.car_charging_repository_impl import CarChargingRepositoryImpl


def showChargingUi():
    st.header("업체 별 전기차 충전 요금")
    charging_repo = CarChargingRepositoryImpl()
    usecase = GetChargingFeesUseCase(charging_repo)

    try:
        df = usecase.execute()
        select_multi = st.sidebar.multiselect("확인하고자 하는 요금 정보를 선택해주세요.", df.columns.tolist())

        st.table(df)
        start_button = st.sidebar.button("요금 조회")

        if start_button:
            if select_multi:
                selected_df = df[select_multi]
                st.table(selected_df)
            else:
                st.warning("조회할 항목을 선택하세요.")
    except Exception as e:
        st.error(f"충전 요금 데이터를 불러오지 못했습니다: {e}")
