import streamlit as st
import plotly.express as px
from regions.domain.usecases import GetRegionDataUseCase
from regions.infra.region_repository_impl import RegionRepositoryImpl

def showRegionsUi():
    st.header("지역별 전기차 등록 대수 현황")
    region_repo = RegionRepositoryImpl()
    usecase = GetRegionDataUseCase(region_repo)

    try:
        df = usecase.execute()
        select_region = st.sidebar.selectbox("확인하고 싶은 지역을 선택하세요", df["region"].unique())

        col1, col2 = st.columns([2, 3])
        with col1:
            st.table(df.head(10))
        with col2:
            fig = px.pie(df, names="region", values="ratio", hole=0.3)
            fig.update_traces(textposition="inside", textinfo="percent+label")
            st.plotly_chart(fig)

        st.header("특정 지역 현황")
        filtered_df = df[df["region"] == select_region]
        st.table(filtered_df.head())
    except Exception as e:
        st.error(f"지역 데이터를 불러오지 못했습니다: {e}")
