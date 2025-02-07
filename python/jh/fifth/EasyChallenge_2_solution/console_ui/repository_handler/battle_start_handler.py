from turn.repository.turn_repository_impl import TurnRepositoryImpl


class BattleStartHandler:

    __turnRepository = TurnRepositoryImpl.getInstance()

    @classmethod
    def processUserInputOnBattle(self):
        turn = self.__turnRepository.getTurn()
        print(f"현재 {turn.getTurnCount()} 턴 진행중입니다.")

        userInput = int(input("선택: "))
        return userInput
