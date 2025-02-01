from game.service.game_service_impl import GameServiceImpl

# Dice game을 시작한다
# 2명 이상의 플레이어를 생성한다
# 플레이어들이 1번째 주사위를 굴린다
# 주사위 번호가 짝수인 플레이어들을 선별한다
# 해당 플레이어가 2번째 주사위를 굴린다
# 주사위 번호와 일치하는 스킬을 적용한다
# 승자를 확인한다

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.rollFirstDice()
gameService.printCurrentStatus()
gameService.rollSecondDice() # 각 플레이어의 첫번째 주사위가 모두 홀수이면 Status()가 연속 호출된다
gameService.printCurrentStatus()
gameService.applySkill()
gameService.printCurrentStatus()
gameService.checkWinner()
