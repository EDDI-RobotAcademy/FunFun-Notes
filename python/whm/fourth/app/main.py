#import random

#i=4
#while 0<i<=4:
 #   card = random.randint(1, 10)
  #  you=input("뽑으시겠습니까?")
   # if you=="yes":
    #    print(card)
     #   if card==3 or card==7:
      #      print("you win!")
       #     break
        #elif card==4:
         #   print("you dead")
          #  break
        #i-=1

     #   if i == 0:
      #      print("you lose")
   # else:
    #    print("개소리야")
    #continue

#카드뽑는건 랜덤
#4턴안에 3 또는 7 뽑기
#4는 죽음
#전적관리

from card.entity.card import Card
from card.repository.card_repository import CardRepository
from card.repository.card_repository_impl import CardRepositoryImpl
from turn.entity.turn import Turn
from turn.repository.turn_repository import TurnRepository
from turn.repository.turn_repository_impl import TurnRepositoryImpl
from game.service.service_repository_impl import GameServiceImpl

gameService=GameServiceImpl.getInstance()
gameService.startGame()
#cardGame=CardRepositoryImpl.getInstance()
#gameTurn=TurnRepositoryImpl.getInstance()
#gameTurn.selectTurn()
#cardGame.selectCard()
