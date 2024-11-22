from dice.repository.dice_repository_impl import DiceRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()
diceRepository.rollDice()
diceRepository.rollDice()
diceList = diceRepository.acquireDiceList()

for dice in diceList:
    print(dice)
