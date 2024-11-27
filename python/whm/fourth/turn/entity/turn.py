class Turn:

    def __init__(self,number):
        self.__number = number


    def __str__(self):
        return f"지금 {self.__number}번쨰 턴 입니다"

    def getTurn(self):
        return self.__number