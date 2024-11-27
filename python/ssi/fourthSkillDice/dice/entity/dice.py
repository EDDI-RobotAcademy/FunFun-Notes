from dice.entity.dice_kinds import DiceKinds


class Dice:
    __counter = 1

    def __init__(self, diceNumber, diceKinds: DiceKinds = DiceKinds.GENERAL):
        self.__number = diceNumber
        self.__id = Dice.__counter
        Dice.__counter += 1
        self.__diceKinds = diceKinds

    def __str__(self):
        return f"dice number: {self.__number}"

    def getId(self):
        return self.__id

    def getDiceNumber(self):
        return self.__number
    
    def setDiceNumber(self, number):
        self.__number = number

    def setDiceKinds(self, diceKinds):
        self.__diceKinds = diceKinds
