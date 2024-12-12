from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__records = []  # 게임 기록 저장
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def recordGame(self, gameResult):
        """게임 결과를 기록"""
        self.__records.append(gameResult)

    def getRecords(self):
        """모든 게임 기록 반환"""
        return self.__records
