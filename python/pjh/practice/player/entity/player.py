import random

class Player:
    START = 0
    END = 3
    __sportList = ["tennis", "football", "baseball", "basketball"]

    def __init__(self):
        self.__selectedSport = self.pickSport()

    def pickSport(self):
        index = random.randint(self.START, self.END)
        return self.__sportList[index]

    def __str__(self):
        return f"Player - selected sport: {self.__selectedSport}"
