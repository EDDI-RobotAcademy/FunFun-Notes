from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl
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
for i in range(len(Team)):
    diceRepository.rollDice()
#플레이어 리스트 길이만큼 주사위 굴리기
for dice in diceList:
    print(dice)
#주사위 결과 리스트 출력

for player in Team:
    print(player)
#Team 리스트 출력

Sum=diceRepository.sumDiceNumber()
print(Sum)







