from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from twodice.repository.twodice_repository_impl import TwoDiceRepositoryImpl

playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createName("Kim")  # player 1
playerRepository.createName("Lee")  # player 2
playerRepository.createName("Yang")  # player 3

twoDiceRepository = TwoDiceRepositoryImpl.getInstance()
twoDiceRepository.rollDice()
twoDiceRepository.rollDice()
twoDiceRepository.rollDice()


playerList = playerRepository.acquirePlayerNameList()

for player in playerList:
    print(player)

# 게임 실행
gameService = GameServiceImpl.getInstance()
gameService.startDiceGame()  # 주사위 굴리기 게임 시작
gameService.rollFirstDice()  # 첫번째 굴리기
gameService.rollSecondDice() # 짝수번째 값 나온 플레이어들만 또 굴리기
gameService.checkWinner()    # 우승자 가리기

