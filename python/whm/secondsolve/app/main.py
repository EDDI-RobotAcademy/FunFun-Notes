from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

#dice파일에 repository파일에 dice_repository_impl이라는 파이썬파일안에 DiceRepositoryImpl을 가져옴

diceRepository = DiceRepositoryImpl.getInstance()
diceNumber = diceRepository.rollDice()
print(diceNumber)
playerRepository=PlayerRepositoryImpl.getInstance()
playerName=playerRepository.Sign()
print(playerName)

