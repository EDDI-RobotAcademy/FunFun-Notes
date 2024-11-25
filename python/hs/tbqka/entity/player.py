# Entity: Player 클래스
class Player:
    def __init__(self, name):
        self.name = name  # 플레이어 이름
        self.dice = []  # 굴린 주사위들

    def roll_dice(self, num_rolls=1):
        """주사위를 여러 번 굴리기"""
        self.dice.clear()  # 이전 주사위 값 초기화
        for _ in range(num_rolls):
            dice = Dice()  # 주사위 객체 생성
            dice.roll()  # 주사위 굴리기
            self.dice.append(dice)

    def get_total(self):
        """주사위 눈금들의 합을 반환"""
        return sum(dice.number for dice in self.dice)  # 주사위 값 합산
