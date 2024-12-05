from game.repository.game_repository import GameRepository
from game.entity.game import Game

class GameRepositoryImpl(GameRepository):
    __instance = None
    __gameList = []   # List
    __skillAppliedPlayerDict = {} # 첫번째 rollDice에서 짝수가 나온 Player의 이름이 담긴 List
    #__nameList = []   # Player들의 이름만 들어있는 List
    #__playerScoreList = []   # Player들의 점수만 들어있는 List

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
        game = Game(playerNameList, eachPlayerDiceList)  # Game 객체 생성
        self.__gameList.append(game)   # gameList = [game]



    def rollFirstDice(self):
        game = self.__gameList[0]
        gameMapInfo = game.getGameMap()     # 게임의 결과, gameMapInfo가 Dictionary로 구성되어 있음.

# e.g) gameMapInfo= {'Kim': 2, 'Lee': 3, 'Yang':6}
# gameMapInfo.items()은 [('Kim', 2), ('Lee', 3), ('Yang',6)] 형태를 반환함
        #for player,dice in gameMapInfo.items():  dice=2
            #self.__nameList.append(player)
            #if dice.getDiceNumber() % 2 == 0:

        __skillAppliedPlayerDict = {key: value for key, value in gameMapInfo.items() if dice.getDiceNumber() % 2 == 0}
                #self.__skillAppliedPlayerList.append(player) # 나중에 player에서 dictionary에 dice 결과 값을 다시 검색
# __skillAppliedPlayerList = ['Kim','Yang'] 이렇게 출력/  __skillAppliedValueList
# __skillAppliedPlayerDict = {'kim':4, 'Yang':3} 주사위 값이 이렇게 나왔다면,


    def rollSecondDice(self):
        for key in __skillAppliedPlayerDict.keys():

            if __skillAppliedPlayerList[key] == 3:  # 모든 상대 점수 -2, 내 점수 +4
                for value in
                self.__gameList[]



            if __skillAppliedPlayerList[key] == 4:
                eliminated_number = input("Write the number of the player who you want to get rid of")
    # e.g) gameList= {'Kim': 2, 'Lee': 3, 'Yang':6}  -> 만약 number가 3 이라면 -> 'Yang' 탈락
                eliminated_player = self.__nameList[eliminated_number-1]
                self.__nameList.remove(eliminated_player)  # 탈락된 Player를 반영한 List






    def checkWinner(self):
        game = self.__gameList[0]
        gameMapInfo = game.getGameMap()

        # Dictionary의 key 값 다 뽑기
        gameMapKeyList = gameMapInfo.keys()
        # Dictionary의 value 값 다 뽑기
        gameMapValueList = gameMapInfo.values()
        # Dictionary의 key, value 값 다 뽑기
        keyValueList = list(gameMapInfo.items())

        print(f"gameMapKeyList: {gameMapKeyList}")
        print(f"gameMapValueList: {gameMapValueList}")
        print(f"keyValueList: {keyValueList}")

        for player, dice in gameMapInfo.items():
            print(f"{player}, dice: {dice.getDiceNumber()}")

        # 람다 방식은 자체적으로 리스트나 어떤 반복적인 요소에서 개별적인 요소를 쪼개서 진행됩니다.
        # key로 player 객체를 선택하고 거기 있는 Dice의 번호를 가져와서 비교시키는 코드입니다.
        # Dictionary에서 value 가져오는 부분 -> gameMapInfo[player]
        winner = max(gameMapInfo, key=lambda player: gameMapInfo[player].getDiceNumber())
        # map에서 각각의 key, value 쌍을 순회하면서 아래의 if 조건에 만족하는 정보만 추려냅니다.
        maxPlayerList = [player for player, dice in gameMapInfo.items()
                        if dice.getDiceNumber() == gameMapInfo[winner].getDiceNumber()]

        maxPlayerCount = len(maxPlayerList)
        if maxPlayerCount > 1:
            print("무승부입니다!")
            return

        print(f"winner: {winner}")



        # Alt + Insert : Override 추가
