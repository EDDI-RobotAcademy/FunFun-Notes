from player.repository.player_repository import PlayerRepository
from player.entity.player import Player

class PlayerRepositoryImpl(PlayerRepository):
    __instance = None

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance
    #싱글톤 생성

    #두명의 선수 이름 받기
    def Sign(self):
        self.name1=input("Insert your name:")
        self.name2=input("Insert your name:")
        player1=Player(self.name1)
        player2=Player(self.name2)
        return Player.getName()
