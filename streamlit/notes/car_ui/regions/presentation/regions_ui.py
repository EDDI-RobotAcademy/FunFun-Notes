import streamlit as st
import plotly.express as px

from regions.domain.usecase import GetRegionDataUseCase
from regions.infra.car_region_repository_impl import CarRegionRepositoryImpl


def showRegionsUi():
    st.header("지역별 전기차 등록 대수 현황")
    region_repo = CarRegionRepositoryImpl()
    usecase = GetRegionDataUseCase(region_repo)

    try:
        df = usecase.execute()
        df.rename(columns={"지역1": "region", "등록대수1": "count", "등록대수2": "ratio"}, inplace=True)

        st.write("execute() 결과 데이터프레임:")
        st.dataframe(df, use_container_width=True, height=600)

        col1, col2 = st.columns([2, 3])
        with col1:
            st.table(df.head(10))
        with col2:
            fig = px.pie(df, names="region", values="ratio", hole=0.3)
            fig.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig)

    except Exception as e:
        st.error(f"지역 데이터를 불러오지 못했습니다: {e}")
