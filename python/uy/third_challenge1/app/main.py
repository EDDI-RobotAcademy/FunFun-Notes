
from twodice.repository.twodice_repository_impl import TwoDiceRepositoryImpl
from twodice.entity.twodice import TwoDice

twodiceRepository = TwoDiceRepositoryImpl.getInstance()

# dice1 = TwoDice()
# dice2 = TwoDice()
## 주사위를 두 개를 생성
# dice1.rollDice()
# dice2.rollDice()
## 총 4번 돌렸음

twodiceRepository.rollDice()

#diceRepository.acquireDiceList()
numList = twodiceRepository.acquireDiceList()
for num in numList:
    print(num.getDiceNumber())

#print(result)

result = twodiceRepository.sum()
print(result)


