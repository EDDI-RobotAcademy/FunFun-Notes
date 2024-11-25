class Dice:

    def __init__(self, diceNumber):
        self.__number = diceNumber
        #self값 초기화 후 __number 대입 거기에 diceNumber값 주입

    def __str__(self):
        return f"dice number: {self.__number}"
        #__number값 출력

    def getDiceNumber(self):
        return self.__number
    #__number값 가져오기