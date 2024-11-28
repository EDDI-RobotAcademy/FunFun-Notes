class Turn:

    def __init__(self):
        self.__number = 0


    def __str__(self):
        return f"지금 {self.__number}번쨰 턴 입니다"

    def getTurn(self):
        return self.__number

    def addTurn(self):
        self.__number+=1