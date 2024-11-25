from dice.repository.dice_repository_impl import DiceRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()
diceNumber = diceRepository.rollDice()
print(diceNumber)
