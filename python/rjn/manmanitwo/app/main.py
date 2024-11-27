from game.service.game_service_impl import gameServiceImpl

gameService = gameServiceImpl.getInstance()
gameService.cardGameStart()
gameService.gameRecord()