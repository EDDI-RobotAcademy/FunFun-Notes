import random


class Player:
    def __init__(self):
        self.__nickName = "유제나"


    def __selectRandomNickName(self):
        selectedIndex = random.randint(1,2)

    def __str__(self):
        return f"player : {self.__nickName}"




