from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

# 2명 이상의 플레이어가 게임을 즐길 것이고
# 주사위를 굴려서 주사위 합이 큰 사람이 이길 것이다.
# 이러한 게임을 만들 것이다.


playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createNumAndName()

# player name list 생성 확인
# playerList = playerRepository.acquirePlayerNameList()
#
# for player in playerList:
#     print(player)

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()

# player 의 dice list  생성 확인
# DiceRepository = DiceRepositoryImpl.getInstance()
# t = DiceRepository.acquireDiceList()
# print(*t)

gameService.checkWinner()