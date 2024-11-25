# Main: 게임 실행 클래스
class DiceGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.repository = DiceRepository()  # 주사위 저장소 객체 (필요한 경우 확장 가능)

    def play(self, num_rolls=1):
        """두 플레이어가 주사위를 굴리고 결과를 출력"""
        # 플레이어 1이 주사위 굴리기
        self.player1.roll_dice(num_rolls)
        # 플레이어 2가 주사위 굴리기
        self.player2.roll_dice(num_rolls)

        # 각 플레이어의 합산 결과
        player1_sum = self.player1.get_total()
        player2_sum = self.player2.get_total()

        # 결과 출력
        print(f"{self.player1.name}의 주사위 합: {player1_sum}")
        print(f"{self.player2.name}의 주사위 합: {player2_sum}")

        # 승자 결정
        if player1_sum > player2_sum:
            print(f"{self.player1.name}가 이겼습니다!")
        elif player1_sum < player2_sum:
            print(f"{self.player2.name}가 이겼습니다!")
        else:
            print("무승부입니다!")
# 게임 실행
if __name__ == "__main__":
    # 두 명의 플레이어 생성
    game = DiceGame("플레이어 1", "플레이어 2")

    # 주사위 굴리기 및 게임 진행
    game.play(num_rolls=2)  # 예: 각 플레이어가 2번씩 주사위 굴림
