

class Card:
    #cardNumList = []
# 총 10장의 카드, 각 카드는 1 ~ 10까지 숫자가 적혀 있다
    def __init__(self, cardNumber):
        self.__cardNumber = cardNumber
        #self.__cardList = [number for number in list(range(1, 11))]


    def __str__(self):
        return f"Card number: {self.__cardNumber}"

