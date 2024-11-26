from game.service.game_service_impl import GameServiceImpl


gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollFirstDice()
gameService.rollSecondDice()
gameService.applySkill()
gameService.checkWinner()
