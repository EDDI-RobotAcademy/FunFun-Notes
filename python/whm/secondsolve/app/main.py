from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
#dice파일에 repository파일에 dice_repository_impl이라는 파이썬파일안에 DiceRepositoryImpl을 가져옴

playerRepository=PlayerRepositoryImpl.getInstance()
#플레이어레포지티에서 싱글톤 사용
playerRepository.Sign()
#플레이어 이름 받기
Team=playerRepository.acquireTeam()
#Team에 플레이어 이름 리스트받기

diceRepository = DiceRepositoryImpl.getInstance()
#주사위 굴리기 싱글톤 사용
diceList=diceRepository.acquireDiceList()
#주사위 굴리기 값 리스트

#플레이어 리스트에 있는 이름들 뽑기(player entity에서 __str__뽑기)
for player in Team:
    print(player)

#플레이어 리스트 길이만큼 주사위 굴리기
for i in range(len(Team)):
    diceRepository.rollDice()

# 주사위 결과 리스트 출력(dice entity에서 __str__뽑기)
#for dice in diceList:
    #print(dice)

#두 명의 플레이어가 게임
#주사위를 굴려 주사위 합이 큰 사람 승리

# 아래처럼 '무엇'을 할 것인지 먼저 작성
gameService=GameServiceImpl.getInstance()
gameService.startDiceGame()
gameService.checkWinner()

#숫자 2개의 합
Sum=diceRepository.sumDiceNumber()
print(Sum)







