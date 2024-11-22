from dice.repository.dice_repository_impl import DiceRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()
# 주사위를 2개 굴리기
diceRepository.rollDice()
diceRepository.rollDice()
# 굴린 주사위 리스트 획득
diceList = diceRepository.acquireDiceList()

# 주사위 리스트를 순회하며 출력
for dice in diceList:
    print(dice)
