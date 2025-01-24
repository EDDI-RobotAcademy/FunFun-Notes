class Player:

    def __init__(self):
        self.__nickname = "default_name"

    def setNickname(self, nickname):
        self.__nickname = nickname

    def __str__(self): # player 인스턴스(객체)를 print 로 출력할 수 있게 한다
        return f"player: {self.__nickname}"


