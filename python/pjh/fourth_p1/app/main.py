from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createName()
playerRepository.createName()
playerRepository.createName()

playerList = playerRepository.acquirePlayerNameList()

for player in playerList:
    print(player)

gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.checkWinner()
gameService.useFirstskill()

# 주사위 굴림
# > 스킬 주사위 활성화 (활성화 된 플레이어 리스트 만듦)
# > 스킬 주사위가 활성화된 플레이어끼리 스킬 주사위 굴림
# > 스킬1 발동
# > 스킬2 발동
# > 최종 결과 리스트업
# > 승자 결정