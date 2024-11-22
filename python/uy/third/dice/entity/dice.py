
class Dice:

    def __init__(self,diceNumber):
        self.__number = diceNumber
        # diceNumber를 받음

    def __str__(self):
        return f"dice number: {self.__number}"

    def getDiceNumber(self):
        return self.__number