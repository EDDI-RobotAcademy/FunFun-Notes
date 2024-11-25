from dice.entity.dice import Dice
from dice.repository.dice_repository_impi import DiceRepositoryImpl
from player.entity.player import Player

print("Our Second Class")

dice = Dice()
dice.rollDice()
dice.printResult()


diceRepository = DiceRepositoryImpl.getInstance()

print(f"문제없이실행이 됩니다 : {diceRepository}")

diceRepository2 = DiceRepositoryImpl.getInstance()

print(f"diceRepository2 : {diceRepository2}")
diceRepository3 = DiceRepositoryImpl.getInstance()

print(f"diceRepository3 : {diceRepository3}")


#같은 애들! interface는 어디에서 임포트 해와도 같다!

player = Player()
print(player)