from game.service.game_service_impl import GameServiceImpl

# 2명 이상의 플레이어를 생성한다
# 플레이어가 1번째 주사위를 굴린다
# 첫번째 플레이어의 주사위가 짝수이면 skill 적용
# 플레이어가 2번째 주사위를 굴린다
# 승자를 확인한다

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollFirstDice()
# gameService.printCurrentStatus()
gameService.rollSecondDice()
# gameService.printCurrentStatus()
gameService.applySkill()
# gameService.printCurrentStatus()
gameService.checkWinner()
