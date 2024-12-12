from card.repository.card_repository_impl import CardRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from game.service.game_service import GameService


class GameServiceImpl(GameService):
    __instance = None

    __gameResult = {}
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__cardRepository = CardRepositoryImpl.getInstance()
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def startCardGame(self):
        print("Card Game Start!")

        self.__gameResult = {"gameId": len(self.__gameRepository.getRecords()) + 1, "turns": []}

        for turn in range(1, 5):  # 최대 4턴
            print(f"\n[Turn {turn}]")
            card = self.__cardRepository.pickCard()  # 카드 뽑기
            print(f"Picked Card: {card}")

            # 결과 판정
            if card.getCardNumber() in [3, 7]:  # 승리 조건
                print("넌 이겼어!")
                self.__gameResult["turns"].append({"turn": turn, "result": "승리"})
                self.__gameRepository.recordGame(self.__gameResult)
                return

            if card.getCardNumber() == 4:  # 패배 조건
                print("넌 졌어!")
                self.__gameResult["turns"].append({"turn": turn, "result": "패"})
                self.__gameRepository.recordGame(self.__gameResult)
                return

            print("No Result. Continue!")
            self.__gameResult["turns"].append({"turn": turn, "result": "Continue"})

        print("Game Over! Max Turns Reached.")
        self.__gameResult["turns"].append({"turn": 4, "result": "Max Turns Reached"})
        self.__gameRepository.recordGame(self.__gameResult)

    def showGameRecords(self):
        print("\nGame Records:")
        for record in self.__gameRepository.getRecords():
            print(f"Game {record['gameId']}:")
            for turn in record["turns"]:
                print(f" {turn['turn']}번째 게임에서 {turn['result']}하였습니다.")
