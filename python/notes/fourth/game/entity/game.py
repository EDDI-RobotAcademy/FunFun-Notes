class Game:
    # HashMap(Dictionary) 생성은 아래와 같이 '중괄호' 를 표기하여 생성할 수 있습니다.
    # Key와 Value 형태로 구성되며 Key 값을 주면 Value가 나오게 됩니다.
    __gameMap = {}

    def __init__(self, playerList, eachPlayerDiceList):
        # 현재 케이스에서는 Key 값이 Player 객체
        # Value 값은 Dice 객체인 상황입니다.
        # zip의 경우엔 각각의 리스트를 하나로 묶어서 처리할 때 아래와 같은 형태로 사용합니다.
        for player, eachPlayerDice in zip(playerList, eachPlayerDiceList):
            # key 로 player를 선택하고 value로 eachPlayerDice를 선택
            self.__gameMap[player] = eachPlayerDice

        print(f"self.gameMap: {self.__gameMap}")

    def getGameMap(self):
        return self.__gameMap
