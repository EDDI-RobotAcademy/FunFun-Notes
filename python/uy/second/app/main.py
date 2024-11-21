from second.dice.entity.dice import Dice
from second.dice.repository.dice_repository_impl import DiceRepositoryImpl
from second.player.entity.player import Player

print("Our Second Class")

dice = Dice()
dice.rollDice()
dice.printResult()

diceRepository = DiceRepositoryImpl.getInstance()
print(f"문제 없이 실행 되니?: {diceRepository}")

diceRepository2 = DiceRepositoryImpl.getInstance()
print(f"diceRepository2: {diceRepository2}")
diceRepository3 = DiceRepositoryImpl.getInstance()
print(f"diceRepository3: {diceRepository3}")

player = Player()
# 경로 설정 주의

