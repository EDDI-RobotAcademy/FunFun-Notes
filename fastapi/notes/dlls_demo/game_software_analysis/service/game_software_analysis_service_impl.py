import pandas as pd

from game_software_analysis.repository.game_software_analysis_repository_impl import GameSoftwareAnalysisRepositoryImpl
from game_software_analysis.service.game_software_analysis_service import GameSoftwareAnalysisService


class GameSoftwareAnalysisServiceImpl(GameSoftwareAnalysisService):
    def __init__(self):
        self.__gameSoftwareAnalysisRepository = GameSoftwareAnalysisRepositoryImpl()

    async def requestAnalysis(self, filePath: str):
        data = self.__gameSoftwareAnalysisRepository.loadDataFromFile(filePath)

        if data is None:
            raise Exception("Error reading data from the file.")

        # 연령대별 분석 수행
        analysisResult = self.__gameSoftwareAnalysisRepository.analyzeAgeGroupData(data)

        graphImagePath = self.__gameSoftwareAnalysisRepository.plot_average_purchase_cost(analysisResult)

        # 결과 및 그래프 경로 반환
        return {"analysisResult": analysisResult.to_dict(orient='records'), "graphImagePath": graphImagePath}
