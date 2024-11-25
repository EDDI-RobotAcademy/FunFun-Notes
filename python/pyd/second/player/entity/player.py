import random


# 클래스 생성 시 class 키워드를 붙여야 합니다
# 생성하고자 하는 클래스 이름은 Dice 입니다.
# 사실상 class를 Domain으로 바라봐야 합니다.
# 이전에 이야기 했듯이 비즈니스 상에서 주요 항목들입니다.
class Player:
    # 보편적으로 대문자만으로 적는 것들 (상수값)
    NAMES = ["예닮", "예담", "예지", "예서"]
    MIN = 1
    MAX = 6

    # 생성자 (클래스를 만들어줌)
    def __init__(self):
        self.__number = "아무개"

    # 주사위를 굴리는 행위
    def rollPlayer(self):
        self.__number = random.randint(self.MIN, self.MAX)

    # 내용 출력
    def printResult(self):
        # f"문자열 {}" 형식의 경우
        # 내부에 있는 변수 정보를 문자열로 만들어줍니다.
        print(f"Player number: {self.__number}")
        print(f"Player names: {', '.join(self.NAMES)}")
