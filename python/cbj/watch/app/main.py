from game.service.game_service_impl import GameServiceImpl
# game_service_impl에서 GameServiceImpl class를 가져옴.

gameService = GameServiceImpl.getInstance()
# GameServiceImpl의 싱글톤을 반환
gameService.startDiceGame()
# 다이스게임을 시작
gameService.rollFirstDice()
# 첫번째 주사위를 굴림
gameService.printCurrentStatus()
# 첫번째 주사위의 Status를 출력
gameService.rollSecondDice()
# 두번째 주사위를 굴림
gameService.printCurrentStatus()
# 두번째 주사위까지의 Status를 출력
gameService.applySkill()
# 스킬을 적용
gameService.printCurrentStatus()
# 스킬이 적용된 Status를 출력
gameService.checkWinner()
# Winner 확인