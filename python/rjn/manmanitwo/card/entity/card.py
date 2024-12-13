class Card:
    def __init__(self, cardNumber):
        self.__cardNumber = cardNumber

    def getCardNumber(self):
        return self.__cardNumber

    def __str__(self):
        return f"Card({self.__cardNumber})"
