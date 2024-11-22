class Dice:

    def __init__(self, diceNumber):
        self.__number = diceNumber

    def printResult(self):
        print(f"dice number: {self.__number}")

    def getDiceNumber(self):
        return self.__number
