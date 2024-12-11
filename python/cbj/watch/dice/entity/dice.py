from dice.entity.dice_kinds import DiceKinds
# dice_kinds에서 DiceKinds class를 가져옴

class Dice:
    __counter = 1
# Dice class생성
    # 이름 맹글링

    def __init__(self, diceNumber, diceKinds: DiceKinds = DiceKinds.GENERAL):
    # Dice class의 diceNumber, diceKinds 생성 및 초기화, DiceKinds = 일반다이스종류
        self.__number = diceNumber
        # 다이스 숫자의 고유 숫자
        self.__id = Dice.__counter
        # 각각의 다이스의 고유 숫자부여
        Dice.__counter += 1
        # 다이스의 카운터는 1씩 늘어남
        self.__diceKinds = diceKinds
        # 다이스의 종류를 부여

    def __str__(self):
        return f"dice number: {self.__number}"
    #

    def getId(self):
        return self.__id

    def getDiceNumber(self):
        return self.__number

    def setDiceKinds(self, diceKinds):
        self.__diceKinds = diceKinds

    def setDiceNumber(self, diceNumber):
        self.__number = diceNumber
