import pandas as pd

from feature_engineering.repository.feature_engineering_repository_impl import FeatureEngineeringRepositoryImpl
from feature_engineering.service.feature_engineering_service import FeatureEngineeringService


class FeatureEngineeringServiceImpl(FeatureEngineeringService):
    __houseData = {
        'date': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01'],
        'size': [2000, 1500, 1800, 2200, 1600],
        'numberOfRooms': [4, 3, 3, 5, 3],
        'age': [10, 15, 12, 5, 20],
        'price': [500000, 450000, 480000, 600000, 430000]
    }

    def __init__(self):
        self.__featureEngineeringRepository = FeatureEngineeringRepositoryImpl()

    async def featureEngineering(self):
        dataFrame = pd.DataFrame(self.__houseData)
        cleanedDataFrame = self.__featureEngineeringRepository.removeUselessInformation(dataFrame)
        handledDataFrame = self.__featureEngineeringRepository.handleMissingValues(cleanedDataFrame)
        X_train, X_test, y_train, y_test = (
            self.__featureEngineeringRepository.splitTrainTestData(handledDataFrame))

        featureEngineeringModel = self.__featureEngineeringRepository.trainModel(X_train, y_train)
        mseError, y_prediction = self.__featureEngineeringRepository.evaluateModel(
            featureEngineeringModel, X_test, y_test)
        print(f"mseError: {mseError}, y_prediction: {y_prediction}")

        comparison = self.__featureEngineeringRepository.compareResult(y_test, y_prediction)
        return comparison
    