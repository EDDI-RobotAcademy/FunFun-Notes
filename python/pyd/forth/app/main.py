from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()
diceRepository.rollDice()
diceRepository.rollDice()
diceRepository.rollDice()

diceList = diceRepository.acquireDiceList()

for dice in diceList:
    print(dice)

playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createName()
playerRepository.createName()
playerRepository.createName()

playerList = playerRepository.acquirePlayerNameList()

for player in playerList:
    print(player)
gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.checkWinner()