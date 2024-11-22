from dice.dice import dice
from repository.dice_repository_impl import DiceRepositoryImpl
from repository.PlayerRepository_Impl import PlayerRepositoryImpl


Dice=dice()
Dice.rollDice()
Dice.result()

dicerepository=DiceRepositoryImpl.getInstane()
print(f"문제없이 실행되나?{dicerepository}")
dicerepository2=DiceRepositoryImpl.getInstane()
print(f"문제없이 실행되나?{dicerepository2}")

Player=PlayerRepositoryImpl.getInstane()
Play1=Player.Sign()
Play2=Player.Sign()
print(f"Player1: {Play1}")
print(f"Player2: {Play2}")