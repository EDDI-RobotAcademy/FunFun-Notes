from dice.repository.dice_repository_impl import DiceRepositoryImpl

repository = DiceRepositoryImpl.getInstance()

repository.rollDice()
diceList = repository.acquireDiceList()
print(*diceList)

repository.rollMultiDice(3)
diceList = repository.acquireDiceList()
print(*diceList)

# 입력 받은 수 만큼 주사위 굴리기
diceCount = int(input("Input Dice Count: "))
repository.rollMultiDice(diceCount)
diceList = repository.acquireDiceList()
print(*diceList)



# for dice in diceList:
#     print(dice)
#
