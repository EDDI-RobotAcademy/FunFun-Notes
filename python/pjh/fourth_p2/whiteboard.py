class Dice:

    def __init__(self, diceKinds):
        self.__diceKinds = diceKinds

    def setDiceKinds(self, diceKinds):
        self.__diceKinds = diceKinds

dice = Dice(5)
dice.setDiceKinds(DiceKinds.SPECIAL)
print(dice)