import random

class Player:
    def __init__(self, name):
        self.name = name
        self.roll_result = 0  # 주사위 결과 저장

    def roll_dice(self):
        """주사위를 굴리고 결과를 저장"""
        self.roll_result = random.randint(1, 6)
        print(f"{self.name} rolled a {self.roll_result}")

# 게임 로직
def play_game(player1, player2):
    """두 플레이어가 주사위를 굴리고 승자를 판별"""
    player1.roll_dice()
    player2.roll_dice()
    
    if player1.roll_result > player2.roll_result:
        print(f"{player1.name} wins!")
    elif player1.roll_result < player2.roll_result:
        print(f"{player2.name} wins!")
    else:
        print("It's a tie!")

# 게임 실행
player1 = Player("Alice")
player2 = Player("Bob")

play_game(player1, player2)