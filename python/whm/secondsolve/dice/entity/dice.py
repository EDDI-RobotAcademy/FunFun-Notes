from dice.entity.dice_kinds import DiceKinds

class Dice:
    __count=1

    def __init__(self, diceNumber, diceKinds: DiceKinds  = DiceKinds.GENERAL):
        self.__number = diceNumber
        self.__id = Dice.__count
        Dice.__count+=1
        self.__diceKinds=diceKinds
        #self값 초기화 후 __number 대입 거기에 diceNumber값 주입

    def __str__(self):
        return f"{self.__number}"
        #__number값 출력

    def getId(self):
        return self.__id

    def getDiceNumber(self):
        return self.__number
    #__number값 가져오기

    def setDiceKinds(self,diceKinds):
        self.__diceKinds=diceKinds

    def setDiceNumber(self,diceNumber):
        self.__number=diceNumber