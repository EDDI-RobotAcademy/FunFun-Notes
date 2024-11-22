from third.dice.repository.dice_repository_impl import DiceRepositoryImpl


diceRepository = DiceRepositoryImpl.getInstance()  # 싱글톤 방식으로 객체를 가져옴

# 주사위를 두번 굴림 => 주사위 2개 생성
diceRepository.rollDice()
diceRepository.rollDice()

# 굴린 주사위 리스트 휙득
diceList = diceRepository.acquireDiceList()


# 주사위 리스트를 순회하며 출력
for dice in diceList:
    print(dice)




