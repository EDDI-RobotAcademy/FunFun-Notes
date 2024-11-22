from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()
# 주사위를 2개 굴리기
diceRepository.rollDice()
diceRepository.rollDice()
# 굴린 주사위 리스트 획득
diceList = diceRepository.acquireDiceList()

# 주사위 리스트를 순회하며 출력
# for '추출정보 in 리스트:' <- 이러한 형태로 사용할 수 있습니다.
for dice in diceList:
    print(dice)

playerRepository = PlayerRepositoryImpl.getInstance()
playerRepository.createName()
playerRepository.createName()

playerList = playerRepository.acquirePlayerNameList()

for player in playerList:
    print(player)