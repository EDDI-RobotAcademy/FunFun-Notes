import sys
import os
from tabulate import tabulate

# 프로젝트 루트를 sys.path에 추가
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl


playerRepository = PlayerRepositoryImpl.getInstance()
playerCount = int(input("게임에 참여할 플레이어 수를 입력하세요 : "))

for player in range(playerCount):
    playerRepository.createName()


playerList = playerRepository.acquirePlayerNameList()

# 두 명의 플레이어가 게임을 즐길 것이고
# 주사위를 굴려서 주사위 합이 큰 사람이 이길 것이다.
# 이러한 게임을 만들 것이다.

# 아래와 같이 우리가 '무엇' 을 할 것인지 먼저 적는 것이 DDD를 잘하기 위한 첫 번째 조건
# Repository는 행위(액션) 이었고 좀 더 정확하게 기술적 세부사항을 다룹니다.
# Service는 서로 다른 Domain Repository 들을 적절하게 엮고 연동하기 위한 목적으로 사용합니다.
# 고로 같은 Layer 끼리 호출하면 안됩니다.
# Repository가 Repository 호출 안되고 Service가 Service 호출하는 것 또한 안됩니다.
gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()

gameRepository = gameService._GameServiceImpl__gameRepository  
gameMap = gameRepository._GameRepositoryImpl__gameList[0].getGameMap()  

# 플레이어 정보와 주사위 결과 테이블 생성
playerInfo = [[f"Player #{player.getID()}", player.getName(), gameMap[player].getDiceNumber()]
              for player in playerList]
print("참여하는 플레이어 목록:")
print(tabulate(playerInfo, headers=["Player ID", "Name", "Dice"], tablefmt="pretty"))


gameService.checkWinner()