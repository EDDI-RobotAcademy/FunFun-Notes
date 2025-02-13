from game.service.game_service_impl import GameServiceImpl

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollFirstDice()
gameService.printCurrentStatus()
    # rollFirstDice() 결과 모두 홀수이면 바로 checkWinner()되게 함
gameService.rollSecondDice()
gameService.printCurrentStatus()
gameService.applySkill()
gameService.printCurrentStatus()
gameService.checkWinner()
