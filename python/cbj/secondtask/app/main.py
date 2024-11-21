from dice.enitity.dice import Dice
from dice.repository.dice_repository_impl import DiceRepositoryImpl

dice = Dice()
dice.rollDice()
dice.printResult()

diceRepository = DiceRepositoryImpl.getInstance()
print(F"실행 되는 중?:{diceRepository}")

diceRepository2 = DiceRepositoryImpl.getInstance()
print(f"diceRepository2: {diceRepository2}")
diceRepository3 = DiceRepositoryImpl.getInstance()
print(f"diceRepository3: {diceRepository3}")