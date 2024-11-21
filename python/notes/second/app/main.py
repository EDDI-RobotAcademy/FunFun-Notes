import random

from dice.entity.dice import Dice
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.entity.player import Player
from player.repository.player_repository_impl import PlayerRepositoryImpl

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
print(player)

diceNumber = random.randint(1, 6)
print(f"주사위 값: {diceNumber}")

playerRepository = PlayerRepositoryImpl.getInstance()
player = playerRepository.pickYourRandomNickname()
print(player)