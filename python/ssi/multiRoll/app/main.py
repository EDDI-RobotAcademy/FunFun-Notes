from dice.repository.dice_repository_impl import DiceRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()
diceRepository.rollDiceTwice()

diceList = diceRepository.acquireDiceList()

for dice in diceList:
    print(dice)