from game.repository.game_repository import GameRepository
from game.entity.game import Game

class GameRepositoryImpl(GameRepository):
    __instance=None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance=cls()

        return cls.__instance
    #싱글톤

    def start(self):
        while True:
            status=input("시작하겠습니까?")
            if status=="yes":
                print("Game Start!")
                break
            else:
                print("개소리야")


