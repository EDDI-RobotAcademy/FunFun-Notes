import random

# 클래스 생성 시 class 키워드를 입력해야 함
# 생성하고자 하는 클래스 이름은 Dice
# 사실상 우리가 정의한 class를 Domain으로 생각하고 작업하자.(실무를 위해)
# (Domain은 특정 행동을 하기 위해 만들어야 할 기능들을 의미함)

class Dice:
    # 보편적으로 대문자만으로 적는 것들은 "상수값" 임
    MAX = 6
    MIN = 1

    # 생성자 (클래스를 만들어줌)
    def __init__(self):
        # 초기 주사위의 눈금은 0
        self.__number = 0

    # 주사위 굴리는 행위 를 정의함
    def rollDice(self):
        self.__number = random.randint(self.MIN, self.MAX)

    # 내용 출력
    def printResult(self):
        # 아래의 f"문자열 {}" 형식의 경우, 내부에 있는 변수 정보를 문자열로 만들어줌
        print(f"dice number: {self.__number}")