import sys
import os

# 프로젝트 루트 경로 추가
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from game.service.game_service_impl import GameServiceImpl

gameService = GameServiceImpl.getInstance()

# 플레이어 수 입력 (제한 없음)
while True:
    playerCount = int(input("게임에 참여할 플레이어 수를 입력하세요: "))
    if playerCount > 0:
        break
    print("플레이어 수는 1명 이상이어야 합니다.")  # 음수나 0 방지

gameService.startDiceGame(playerCount)
# gameService.printCurrentStatus()
gameService.rollFirstDice()
# gameService.printCurrentStatus()
gameService.rollSecondDice()
#gameService.printCurrentStatus()
gameService.applySkill()
#gameService.printCurrentStatus()
gameService.checkWinner()