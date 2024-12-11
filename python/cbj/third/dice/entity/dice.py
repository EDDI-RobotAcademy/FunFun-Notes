class Dice:
    MAX = 6
    MIN = 1

    def __init__(self, diceNumber):
        self.__number = diceNumber

    def __str__(self):
        return f"dice number: {self.__number}"

    def getDiceNumber(self):
        return self.__number
