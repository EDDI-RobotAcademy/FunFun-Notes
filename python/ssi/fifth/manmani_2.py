import random


class Card_Game:
    def __init__(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]
        self.turns_left = 4
        self.winning_cards ={3,7}
        self.losing_card = 4
        self.game_record = []

    def reset_game(self):
        self.cards = [1,2,3,4,5,6,7,8,9,10]
        self.turns_left = 4

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

    def start_game(self,game_number):
        print(f"\n-----------------{game_number}번째 게임을 시작합니다!-----------------")

        while self.turns_left > 0:
            self.left_card()
            result = self.play_with_turn()
            self.turns_left -= 1

            if result in {"WIN", "LOSE"}:
                self.game_record.append({
                    "game_number" : game_number,
                    "result" : result,
                    "used_turns" : 4 - self.turns_left
                })
                return result
            
        print("턴을 모두 소모하였습니다... 승리조건을 달성하지 못해 패배하였습니다.")
        self.game_record.append({
            "game_number" : game_number,
            "result" : "LOSE",
            "used_turns" : 4
        })
        return "LOSE"
    
    def show_records(self):
        print("\n-----------------게임 전적-----------------")

        if not self.game_record:
            print("전적이 없습니다")
            return
        
        wins = 0
        
        for record in self.game_record:
            print(f"게임 {record['game_number']} : {record['used_turns']}턴에 {record['result']}")
            if record["result"] == "WIN":
                wins += 1
        
        total_games = len(self.game_record)
        win_rate = (wins/total_games) * 100
        print(f"\n총 게임수 : {total_games}, 승리 : {wins}, 패배 : {total_games - wins}")
        print(f" 승률 : {win_rate:.2f}%")

        # print("카드 게임을 실행합니다!")

        # while self.turns_left > 0:
        #     result = self.play_with_turn()
        #     self.turns_left -= 1

        #     if result in {"WIN","LOSE"}:
        #         return result
            
        #     self.left_card()

        # print("턴을 모두 소모하였습니다... 승리조건을 달성하지 못해 패배하였습니다")
        # return "LOSE"     

if __name__ == "__main__":
    game = Card_Game()
    game_number = 1

    while True:
        print("\n1. 새 게임 시작")
        print("2. 전적 및 승률 보기")
        print("3. 종료")

        choice = input("선택 : ")

        if choice == "1":
            game.reset_game()
            result = game.start_game(game_number)
            game_number += 1
            
            if result == "WIN":
                print("게임 결과 : 승리")
            else:
                print("게임 결과 : 패배")
        
        elif choice == "2":
            game.show_records()
        
        elif choice == "3":
            print("게임을 종료합니다")
            break

        else:
            print("잘못된 입력입니다. 다시 번호를 고르세요")
