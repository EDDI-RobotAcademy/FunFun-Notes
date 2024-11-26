from game.entity.game import Game
from game.repository.game_repository import GameRepository


class GameRepositoryImpl(GameRepository):
    __instance = None
    __gameList=[]
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

    def start(self,playerNameList,eachPlayerDiceList):
        game= Game(playerNameList,eachPlayerDiceList)
        self.__gameList.append(game)

    def checkWinner(self):
        game=self.__gameList[0]
        gameMapINfo=game.getGameMap()

        for player,dicenumber in gameMapINfo.items():
            print(player,"number is",dicenumber)

        #Dictionary의 key값 다 뽑기
        gameMapKeyList=gameMapINfo.keys()
        # Dictionary의 value값 다 뽑기
        gameMapValueList=gameMapINfo.values()
        # Dictionary의 key,value값 다 뽑기
        keyValueList=list(gameMapINfo.items())


        #print(f"gameMapKeyList: {gameMapKeyList}")
        #print(f"gameMapValueList: {gameMapValueList}")
        #print(f"KeyValueList: {keyValueList}")

        #람다 방식은 자체적으로 리스트나 어떤 반복적인 요소에서 개별적인 요소를 쪼개서 진행
        #keys로 player객체를 선택하고 거기있는 Dice의 번호를 가져와서 비교시키는 코드
        #Dictionary에서 value 가져오는 부분 ->gameMApINfo[player]
        winner=max(gameMapINfo,key=lambda player:gameMapINfo[player].getDiceNumber())
        #map에서 각각의 key,value쌍을 순회하면서 아래의 if조건에 만족하는 정보만 추려낸다
        maxPlayerList=[player for player, dice in gameMapINfo.items()
                       if dice.getDiceNumber()==gameMapINfo[winner].getDiceNumber()]

        maxPlayerCount = len(maxPlayerList)
        if maxPlayerCount > 1:
            print("무승부입니다")
            return

        print(f"winner: {winner}")



