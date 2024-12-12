from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service_impl import GameServiceImpl

gameService = GameServiceImpl.getInstance()

gameService.startCardGame()
gameService.startCardGame()
gameService.startCardGame()


gameService.showGameRecords()