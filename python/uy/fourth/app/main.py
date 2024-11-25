from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.service.game_service_impl import GameServiceImpl

playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createName()
playerRepository.createName()

playerList = playerRepository.acquirePlayerNameList()

for player in playerList:
    print(player)

# 두명의 플레이어가 주사위를 던져서 나온 값을 비교해서 누가 이겼는지 판정
# Service는 서로 다른 Domain Repository들을 적절하게 엮고 연동하기 위한 목적으로 사용
# Service -> 여러 repository 쓰기 !가능!
# Repository -> 여러 Repository  불가능
# Service -> 여러 Service 불가능
# Repository -> 여러 Service 불가능

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.checkWinner()

