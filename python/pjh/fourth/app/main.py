from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createName()
playerRepository.createName()

playerList = playerRepository.acquirePlayerNameList()

for player in playerList:
    print(player)

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
gameService.checkWinner()
