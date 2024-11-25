from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
from player.repository.player_repository_impl import PlayerRepositoryImpl


class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # Service Layer에서 Repository Layer를 연결하는 방법
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository = PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def __createGamePlayer(self):
        gamePlayerCount = self.__gameRepository.getGamePlayerCount()


        # 반복실행 문
        # for 반복변수 in  range (반복횟수)  :  빈복실행할 대상
        for _ in range(gamePlayerCount):
            self.__playerRepository.createName()

    def startDiceGame(self):
        print("startDiceGame() called!")
        self.__gameRepository.create()

        self.__createGamePlayer()

    def rollFirstDice(self):
        gamePlayerCount = self.__gameRepository.getGamePlayerCount()

        # 실제 정말 사용자 숫자만큼 반복을 함 (3명이라 가정)
        # 위 가정의 경우 0, 1, 2로 playerIndex가 설정됨
        for playerIndex in range(gamePlayerCount):
            print(f"playerIndex: {playerIndex}")
            # 기존에는 단순히 굴리기만 했음
            # 혹은 굴리고 Dice 객체 자체를 리턴했음
            # 그러나 Player가 어떤 Dice 객체를 소유하고 있는지 판단할 필요가 생겼음
            # 그러므로 rollDice() 이후 생성된 주사위의 고유한 번호(id)를 리턴시켰음
            diceId = self.__diceRepository.rollDice()
            # 위의 인덱스는 0부터 시작하지만 Entity 구성의 id가 1부터 시작함
            # 그러므로 발생한 이격을 조정하기 위해 +1을 해서 검색하고 있음
            # findById()를 통해 검색된 Player 객체를 획득
            indexedPlayer = self.__playerRepository.findById(playerIndex + 1)
            print(f"indexedPlayer: {indexedPlayer}")
            # Player 엔티티에 setDiceId를 구현하여 획득한 주사위의 번호를 설정함
            # 고로 특정 Player가 특정 Dice의 소유권을 확보하게 되었음
            indexedPlayer.addDiceId(diceId)

        for player in self.__playerRepository.acquirePlayerList():
            print(f"{player}")


    def checkWinner(self):
        print("checkWinner() called!")
