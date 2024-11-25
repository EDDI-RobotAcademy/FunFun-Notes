from game.entity.game import Game
from game.repository.game_repository import GameRepository
from tabulate import tabulate

class GameRepositoryImpl(GameRepository):
    __instance = None

    __gameList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def start(self, playerNameList, eachPlayerDiceList):
        game = Game(playerNameList, eachPlayerDiceList)
        self.__gameList.append(game)

    def checkWinner(self):
        # if not self.__gameList:
        #     print("Error: no game in gamelist")
        #     return None
        game = self.__gameList[0]
        gameMapInfo = game.getGameMap()

        # Dictionary의 key 값 다 뽑기
        gameMapKeyList = gameMapInfo.keys()
        # Dictionary의 value 값 다 뽑기
        gameMapValueList = gameMapInfo.values()
        # Dictionary의 key, value 값 다 뽑기
        keyValueList = list(gameMapInfo.items())
        # print(f"gameMapKeyList: {gameMapKeyList}")
        # print(f"gameMapValueList: {gameMapValueList}")
        # print(f"keyValueList: {keyValueList}")

        # 람다 방식은 자체적으로 리스트나 어떤 반복적인 요소에서 개별적인 요소를 쪼개서 진행됩니다.
        # key로 player 객체를 선택하고 거기 있는 Dice의 번호를 가져와서 비교시키는 코드입니다.
        # Dictionary에서 value 가져오는 부분 -> gameMapInfo[player]
        winner = max(gameMapInfo, key=lambda player: gameMapInfo[player].getDiceNumber())
        # map에서 각각의 key, value 쌍을 순회하면서 아래의 if 조건에 만족하는 정보만 추려냅니다.
        maxDiceNumber = gameMapInfo[winner].getDiceNumber()
        maxPlayerList = [player for player, dice in gameMapInfo.items()
                         if dice.getDiceNumber() == maxDiceNumber]
        

        if len(maxPlayerList) > 1:
            print("무승부입니다! 공동 우승자:")
            playerInfo = [[f"Player#{player.getID()}", player.getName(), gameMapInfo[player].getDiceNumber()]
                      for player in maxPlayerList]
            
            print(tabulate(playerInfo, headers = ["Player ID", "Name", "Dice"], tablefmt = "preety"))
            return
        
        print("우승자:")
        playerInfo = [[f"Player #{winner.getID()}", winner.getName(), maxDiceNumber]]
        print(tabulate(playerInfo, headers=["Player ID", "Name", "Dice"], tablefmt= "preety"))