class Fruit:

    def __init__(self,name,number):
        self.__name=name
        self.__number = number

    def __str__(self):
        return f"오늘 들어온 과일은({self.__name},{self.__number}개)입니다"

    def getName(self):
        return self.__name

    def getNumber(self):
        return self.__number