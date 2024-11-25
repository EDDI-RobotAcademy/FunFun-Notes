class Game:
    #HashMap(Dictionary) 생성은 아래와 같이 '중괄호' 줄 표기하여 생성 가능
    #key와 value 형태로 구성되며 key값을 주면 value가 나오게 된다
    __gameMap={}

    def __init__(self, playerNameList,eachPlayerDiceList):
        #현재 케이스에서는 key값이 player객체
        #value 값은 Dice객체
        #zip의 경우엔 각각의 리스트를 하나로 묶어서 처리할 때 아래와 같은 형태로 사용
        for player, eachPlayerDice in zip(playerNameList,eachPlayerDiceList):
            self.__gameMap[player]=eachPlayerDice

            #print(f"self.gameMap: {self.__gameMap}")

    def getGameMap(self):
        return self.__gameMap