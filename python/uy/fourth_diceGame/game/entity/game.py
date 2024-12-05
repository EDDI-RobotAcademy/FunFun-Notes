from player.entity.player import Player
from twodice.entity.twodice import TwoDice


class Game:

    #__gameMap = {Player('Kim'): dice1, Player('Lee'): TwoDice(2), Player('Yang'): TwoDice(6)}
    __gameMap = {}


    #def __init__(self):
        # 플레이어 리스트, 각 플레이어 주사위 결과 리스트
        #for player, eachPlayerDice in zip(playerList, eachPlayerDiceList):
            # Eg) Kim, 5
            #self.__gameMap[player] = eachPlayerDice
            # gameMap[Kim] = 5

        #print(f"self.gameMap: {self.__gameMap}")

    def getGameMap(self):
        return self.__gameMap   #

        # shift + F6 : 변수 다같이 (한꺼번에) 변경
