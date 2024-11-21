from dice.entity.dice import Dice
from dice.repository.dice_repository_impl import DiceRepositoryImpl

print("Our Second Class")

dice = Dice()
dice.rollDice()
dice.printResult()

diceRepository = DiceRepositoryImpl.getInstance()
print(f"실행됨?: {diceRepository}")

diceRepository = DiceRepositoryImpl.getInstance()
print(f": DiceRepository2: {diceRepository}")
diceRepository = DiceRepositoryImpl.getInstance()
print(f": DiceRepository2: {diceRepository}")
