#주사위의 행위 및 굴리기

import random
#사실상 class를 도메인으로 봐야한다
#비즈니스상에서 주요 항목들이다
class dice:
    # 보편적으로 대문자로 적는것들(상수값)
    MAX=6
    MIN=1
    #생성자(클래스를 만들어줌)
    def __init__(self):
        #초기 주사위의 눈금은 0
        self.__num=0
    # 주사위를 굴리는 행위
    def rollDice(self):
        self.__num = random.randint(self.MIN,self.MAX)
    #내용 출력
    def result(self):
        #f"문자열{}"dml의 경우
        #내부에 있는 변수정보를 문자열로 만들어 준다
        print(f"dice number:{self.__num}")