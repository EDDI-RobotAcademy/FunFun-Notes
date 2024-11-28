import sys
import os

# 프로젝트 루트 경로 추가
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)


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
