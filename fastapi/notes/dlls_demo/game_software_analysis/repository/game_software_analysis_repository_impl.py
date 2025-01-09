import os

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import font_manager

from game_software_analysis.repository.game_software_analysis_repository import GameSoftwareAnalysisRepository


class GameSoftwareAnalysisRepositoryImpl(GameSoftwareAnalysisRepository):

    def loadDataFromFile(self, filePath: str) -> pd.DataFrame:
        try:
            data = pd.read_excel(filePath)
            return data
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def analyzeAgeGroupData(self, data: pd.DataFrame):
        # 연령대 계산 (예: 10대, 20대, 30대 등으로 나누기)
        data['age_group'] = data['age'].apply(lambda x: f"{(x // 10) * 10}s")  # 예: 20대, 30대, ...

        # 연령대별로 게임 소프트웨어의 구매 건수와 구매 총액 계산
        ageGroupData = data.groupby(['age_group', 'game_software_title']).agg(
            total_purchase_count=pd.NamedAgg(column='quantity', aggfunc='sum'),
            total_purchase_cost=pd.NamedAgg(column='total_price', aggfunc='sum')
        ).reset_index()

        # 연령대별로 가장 많이 구매한 게임 소프트웨어 정렬
        ageGroupData['average_purchase_cost'] = ageGroupData['total_purchase_cost'] / ageGroupData[
            'total_purchase_count']

        return ageGroupData

    # sudo apt update
    # sudo apt install -y fonts-nanum fonts-noto-cjk
    # sudo apt install fonts-nanum
    def plot_average_purchase_cost(self, ageGroupData: pd.DataFrame):
        # 정확한 한글 폰트 경로 설정
        font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"  # 실제 폰트 경로 확인
        font_prop = font_manager.FontProperties(fname=font_path)

        # matplotlib의 기본 폰트 설정
        plt.rcParams['font.family'] = font_prop.get_name()  # 올바른 폰트 이름 사용
        plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호가 깨지지 않도록 설정

        plt.figure(figsize=(10, 6))

        # 'game_software_title'을 색상별로 구분하는 그래프 그리기
        sns.barplot(data=ageGroupData, x='age_group', y='average_purchase_cost', hue='game_software_title')

        # 제목과 축 레이블 설정
        plt.title('연령대별 평균 구매 금액')
        plt.xlabel('연령대')
        plt.ylabel('평균 구매 금액')

        # x축 레이블 가운데 정렬 및 회전
        plt.xticks(rotation=45, ha='center')

        # 범례 위치를 하단 가운데로 설정
        plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), ncol=3)

        # 그래프 이미지를 파일로 저장
        graph_path = os.path.join(os.getcwd(), "resource", "age_group_purchase_cost.png")
        plt.savefig(graph_path, bbox_inches='tight')  # bbox_inches='tight'로 레이아웃이 잘리는 문제 방지
        plt.close()

        print(f"Graph saved to: {graph_path}")
