import pandas as pd

from ensemble_method.repository.ensemble_method_repository_impl import EnsembleMethodRepositoryImpl
from ensemble_method.service.ensemble_method_service import EnsembleMethodService


class EnsembleMethodServiceImpl(EnsembleMethodService):
    TITANIC_DATA_URL = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
    TARGET_COLUMNS = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]
    MISSING_VALUES_COLUMN = "Age"
    WHICH_ONE_IS_Y_TARGET = "Survived"

    def __init__(self):
        self.__ensembleMethodRepository = EnsembleMethodRepositoryImpl()

    def __loadTitanicData(self):
        return pd.read_csv(self.TITANIC_DATA_URL)

    async def ensembleMethod(self):
        loadedTitanicDataFrame = self.__loadTitanicData()
        preProcessedDataFrame = self.__ensembleMethodRepository.filterColumns(
            loadedTitanicDataFrame, self.TARGET_COLUMNS)

        handledMissingValueDataFrame = self.__ensembleMethodRepository.handleMissingValue(
            preProcessedDataFrame, self.MISSING_VALUES_COLUMN)

        encodedSexDataFrame = self.__ensembleMethodRepository.encodeSexLabel(
            handledMissingValueDataFrame)

        X_train, X_test, y_train, y_test = (
            self.__ensembleMethodRepository.splitTrainTestData(
                encodedSexDataFrame, self.WHICH_ONE_IS_Y_TARGET))

        randomForestModel = self.__ensembleMethodRepository.createRandomForestClassifier()
        gradientBoostModel = self.__ensembleMethodRepository.createGradientBoostClassifier()

        votingModel = self.__ensembleMethodRepository.createVotingModel(
            randomForestModel, gradientBoostModel)

        trainedVotingModel, trainedRandomForestModel, trainedGradientBoostModel =(
            self.__ensembleMethodRepository.trainModel(
                votingModel, randomForestModel, gradientBoostModel,
                X_train, y_train))

        predictedVotingModel, predictedRandomForestModel, predictedGradientBoostModel = (
            self.__ensembleMethodRepository.evaluate(
                trainedVotingModel, trainedRandomForestModel, trainedGradientBoostModel,
                X_test))

        return self.__ensembleMethodRepository.accuracyTest(
            predictedVotingModel, predictedRandomForestModel, predictedGradientBoostModel,
            y_test)
