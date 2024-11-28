from turn.repository.turn_repository_impl import TurnRepositoryImpl
from game.service.service_repository import GameService
from card.repository.card_repository_impl import CardRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl

class GameServiceImpl(GameService):
    __instance = None

    def __new__(cls):
        #진짜 생성자 생성
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            #service layer에서 repository layer를 연결하는 방법
            cls.__instance.__cardRepository=CardRepositoryImpl.getInstance()
            cls.__instance.__turnRepository=TurnRepositoryImpl.getInstance()
            cls.__instance.__gameRepository=GameRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def startGame(self):
        playCount=4
        self.__gameRepository.start()
        self.__turnRepository.createTrun()
        while 0<playCount<=4:
            self.__turnRepository.addTurn()
            self.__turnRepository.selectTurn()
            checkNumber=self.__cardRepository.selectCard()
            playCount-=1

            if checkNumber==3 or checkNumber==7:
                print("you Win!")
                break

            elif checkNumber==4:
                print("you Lose...")
                break

            if playCount==0:
                print("you lose")
