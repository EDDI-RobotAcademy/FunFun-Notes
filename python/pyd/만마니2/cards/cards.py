import random

class CardNumber:
    def __init__(self, card_number):
        self.card_number = card_number

    def cardnumber(self):
        if self.card_number == 3 or self.card_number == 7:
            print("you are winner")

        elif self.card_number == 4:  # 정수 비교
            print("You are dead")
        else:
            print("You have chosen to skip a card")

    def rollcard(self):
        self.card_number = random.randint(1, 10)  # 범위 내의 랜덤 정수 생성
        print(f"Your card number is {self.card_number}")

# 객체 생성 시 card_number를 정수로 전달
card1 = CardNumber(3)
card1.rollcard()  # card_number를 랜덤하게 설정
card1.cardnumber()  # 변경된 card_number 기반으로 출력



