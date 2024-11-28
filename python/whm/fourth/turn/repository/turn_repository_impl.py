from turn.repository.turn_repository import TurnRepository
from turn.entity.turn import Turn

class TurnRepositoryImpl(TurnRepository):
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

    def selectTurn(self):
        myTurn=1
        now=Turn(myTurn)
        print(now)
        myTurn+=1

