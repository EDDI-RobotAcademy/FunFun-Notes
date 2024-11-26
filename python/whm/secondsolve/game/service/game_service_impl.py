from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            #service layer에서 repository layer를 연결하는 방법
            cls.__instance.__gameRepository=GameRepositoryImpl.getInstance()
            cls.__instance.__playerRepository=PlayerRepositoryImpl.getInstance()
            cls.__instance.__diceRepository=DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    #싱글톤 생성


    def startDiceGame(self):
        playerNameList=self.__playerRepository.acquireTeam()
        #playerNameLst는 player딕셔너리의 impl에서 저장해놓은 선수들 리스트
        for i in range(len(playerNameList)):
            self.__diceRepository.rollDice()
        eachPlayerDiceList = self.__diceRepository.acquireDiceList()
        #eachPlayerDiceList는 dice딕셔너리의 impl에서 저장해놓은 주사위숫자 리스트

        self.__gameRepository.start(
            playerNameList, eachPlayerDiceList)

    def rollFirstDice(self):
        gamePlayerCount=len(self.__playerRepository.acquireTeam())
        #gamePlayerCount에 플레이어들 인원수를 추가

        #playerindex가 0~플레이어 인원수만큼 가짐
        #각 Player가 어떤 주사위를 가지고 있는지를 표현
        for playerindex in range(gamePlayerCount):
            diceId = self.__diceRepository.rollDice()
            #diceId에는 주사위를 굴린 숫자가 들어감
            indexedPlayer=self.__playerRepository.findId(playerindex+1)
            #indexedPlayer에는 1번플레이어부터 들어감
            indexedPlayer.addDiceId(diceId)

        for player in self.__playerRepository.acquireTeam():
            print(f"{player}")



    def rollSecondDice(self):
        pass


    def checkWinner(self):
        self.__gameRepository.checkWinner()
