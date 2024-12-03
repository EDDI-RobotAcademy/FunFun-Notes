from dice_game.game.repository.game_repository_impl import GameRepositoryImpl
from dice_game.dice.repository.dice_repository_impl import DiceRepositoryImpl
from dice_game.game.service.game_service import GameServiceRepository


class GameServiceImpl(GameServiceRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__diceRepository=DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def rollDice(self):
        rolled_values = []
        for i in range(1,5):
            dice_data = self.__diceRepository.rollDice()
            rolled_values.append(dice_data)
        return rolled_values

    def __sumDice(self):

        dice_1 = self.__diceRepository.findById(1).number
        dice_2 = self.__diceRepository.findById(2).number
        dice_3 = self.__diceRepository.findById(3).number
        dice_4 = self.__diceRepository.findById(4).number

        sumDice1 = dice_1 + dice_2
        sumDice2 = dice_3 + dice_4

        if sumDice1>sumDice2:
            return sumDice1
        elif sumDice1<sumDice2:
            return sumDice2
        else:
            print("무승부 입니다.")

    def checkWinner(self):
        lastSumNumber=self.__sumDice()
        if lastSumNumber is None:
            print("lastsumnumber is blank")
        return lastSumNumber