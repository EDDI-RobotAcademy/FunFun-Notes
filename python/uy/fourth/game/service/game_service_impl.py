# 1. 사용자 이름 만들기
# 2. 주사위 굴리기
# 3. 주사위 눈 비교해서 승자 가리기

from twodice.repository.twodice_repository_impl import TwoDiceRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # Service Layer에서 Repository Layer를 연결하는 방법/
            # 한 Service에서 모든 repository를 연결
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = TwoDiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def startDiceGame(self):
        print("startDiceGame() called!")
        playerNameList = self.__playerRepository.acquirePlayerNameList()
        self.__diceRepository.rollDice()
        eachPlayerDiceList = self.__diceRepository.rollDice()
        self.__gameRepository.start(playerNameList, eachPlayerDiceList)
        pass

    def checkWinner(self):
        print("checkWinner() called!")
        pass