
# 카드를 4번 뽑아
# 4번안에 3,7이 있으면 Win, 4가 나오면 Fail

from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service_impl import GameServiceImpl
from card.repository.card_repository_impl import CardRepositoryImpl

#gameService = GameServiceImpl.getInstance()
gameService = CardRepositoryImpl.getInstance()
gameService.pickCard()
