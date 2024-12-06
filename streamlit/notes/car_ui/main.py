import streamlit as st

from cars.presentation.car_ui import showCarUi
from charging.presentation.charging_ui import showChargingUi
from regions.presentation.regions_ui import showRegionsUi

st.set_page_config(layout="wide")
st.title("전기차 종합 DB 조회 포털:mag:")

tab1, tab2, tab3 = st.tabs(["차량 정보 조회", "전기차 등록 대수 현황", "업체 별 전기차 충전 요금"])

with tab1:
    showCarUi()

with tab2:
    showRegionsUi()

with tab3:
    showChargingUi()
