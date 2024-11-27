from dice.entity.dice_skill import DiceSkill
from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None
    __game= None

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    #싱글톤 생성


    def create(self):
        while True:
            try:
                playerCount=int(input("몇명이십니까?"))
                if playerCount<=1:
                    print("2인 이상 게임입니다.")
                    continue
                game=Game(playerCount)
                self.__game=game
                break

            except ValueError:
                print("숫자로 적으십시오!")

    def setplayerIndexDiceGameMap(self,playerIndexLsit,diceIdList):
        self.__game.setplayerIndexDiceGameMap(playerIndexLsit,diceIdList)

    def updatePlayerIndexListMap(self,skillAppliedPlayerIndexList,secondDiceIdList):
        self.__game.updatePlayerIndexListMap(skillAppliedPlayerIndexList,secondDiceIdList)

    def deleteTargetPlayerId(self,targetPlayerId):
        self.__game.deleteTargetPlayerId(targetPlayerId)

    def getGamePlayerCount(self):
        return self.__game.getPlayerCount()

    def getGame(self):
        return self.__game