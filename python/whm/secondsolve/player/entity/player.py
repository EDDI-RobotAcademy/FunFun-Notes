class Player():
    A=1

    def __init__(self, name):
        self.__name = name
        #name으로 값 받기

    def __str__(self):
        return f"player: {self.__name}"
    #self.name값 출력

    def getName(self):
        return self.__name
    #self.name값 출력