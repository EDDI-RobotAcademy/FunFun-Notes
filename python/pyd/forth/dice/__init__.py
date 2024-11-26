import random

from player.entity.player import Player
from player.repository.player_repository import PlayerRepository


class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    # 빈 리스트를 생성하여 여기에 주사위 정보를 저장하려고 함
    # 즉 이번 케이스는 rollDice()가 구동 될 때마다 diceList에 내용이 누적됨
    # 빈 리스트를 생성하는 문법입니다.
    __diceList = []



    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollPlayer(self):
        player = Player(diceNumber)
        # append() 붙이기를 통해서
        # 생성자로 만든 dice를 __diceList에 추가하였습니다.
        self.__diceList.append(dice)

    # 누적된 전체 리스트를 가져오게 됨
    def acquirePlayerList(self):
        return self.__playerList