from dice.repository.dice_repository_impl import DiceRepositoryImpl
from player.repository.player_repository_impl import PlayerRepositoryImpl


# 주사위 굴린 것과 플레이어의 이름을 각각 출력하는 프로그램

diceRepository = DiceRepositoryImpl.getInstance()

# 주사위 굴리기
diceRepository.rollDice()
diceRepository.rollDice()
diceRepository.rollDice()

# 굴린 주사위 리스트
diceList = diceRepository.acquireDiceList()

# for '추출정보 in 리스트:' <- 이러한 형태로 사용할 수 있습니다.
for dice in diceList:
    print(dice)


playerRepository = PlayerRepositoryImpl.getInstance()

playerRepository.createName()
playerRepository.createName()
playerRepository.createName()

playerList = playerRepository.acquirePlayerNameList()
                                # dice 리스트와 player 리스트를
                                 # key-value 값으로 묶어 딕셔너리로 출력 가능할 듯
for player in playerList:
    print(player)


