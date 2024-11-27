import random


class Card_Game:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]
        self.turns_left = 4
        self.winning_cards ={3,7}
        self.losing_card = 4

    def draw_card(self):
        if not self.cards:
            raise ValueError("카드가 없습니다")
        card = random.choice(self.cards)
        self.cards.remove(card)
        return card
    
    def left_card(self):
        print("남은 카드 : ")
        print(self.cards)

    def play_with_turn(self):
        #턴 진행
        print(f"\n남은 턴 수 : {self.turns_left}")
        print("카드 뽑는중...")

        card = self.draw_card()

        print(f"뽑은 카드 : {card}")

        if card in self.winning_cards:
            print("축하합니다 승리카드를 뽑았습니다!")
            return "WIN"
        elif card == self.losing_card:
            print("아쉽습니다... 패배카드를 뽑았습니다")
            return "LOSE"
        else:
            print("게임이 계속 됩니다")
            return "CONTINUE"

    def start_game(self):
        print("카드 게임을 실행합니다!")

        while self.turns_left > 0:
            result = self.play_with_turn()
            self.turns_left -= 1

            if result in {"WIN","LOSE"}:
                return result
            
            self.left_card()

        print("턴을 모두 소모하였습니다... 승리조건을 달성하지 못해 패배하였습니다")
        return "LOSE"     

if __name__ == "__main__":
    game = Card_Game()
    result = game.start_game()

    if result == "WIN":
        print("\n게임 결과 : 승리!")
    else:
        print("\n게임 결과 : 패배...")