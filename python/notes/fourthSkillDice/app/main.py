from game.service.game_service_impl import GameServiceImpl


gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollFirstDice()
gameService.printCurrentStatus()
gameService.rollSecondDice()
gameService.printCurrentStatus()
gameService.applySkill()
gameService.printCurrentStatus()
gameService.checkWinner()
