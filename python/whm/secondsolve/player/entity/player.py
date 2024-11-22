class Player():

    def __init__(self, name1, name2):
        self.__name1 = name1
        self.__name2= name2

    def getName(self):
        return self.__name1, self.__name2

    def Result(self):
        print(f"dice number: {self.__number}")
        # __number값 출력