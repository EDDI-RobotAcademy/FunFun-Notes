from game.service.game_service_impl import GameServiceImpl
#dice파일에 repository파일에 dice_repository_impl이라는 파이썬파일안에 DiceRepositoryImpl을 가져옴

# 아래처럼 '무엇'을 할 것인지 먼저 작성
gameService=GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollFirstDice()
gameService.printCurrentStatus()
gameService.rollSecondDice()
gameService.printCurrentStatus()
gameService.applySkill()
gameService.printCurrentStatus()
gameService.checkWinner()









