class Game:

    def __init__(self,number):
        self.__number = number

    def __str__(self):
        return f"당신이 뽑은카드는 {self.__number}입니다"

    def getNumber(self):
        return self.__number