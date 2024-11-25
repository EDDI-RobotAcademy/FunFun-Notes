from dice.repository.dice_repository_impl import DiceRepositoryImpl

diceRepository = DiceRepositoryImpl.getInstance()

dice1 = diceRepository.rollDice()
dice2 = diceRepository.rollDice()


print(f"First dice: {dice1}")
print(f"Second dice: {dice2}")


sum = dice1.getDiceNumber() + dice2.getDiceNumber()
print(f"Sum of dices: {sum}")
