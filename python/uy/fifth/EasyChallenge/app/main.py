# the number of apple and orange
#appleCount = 3
#orangeCount = 5

# 단순 출력
#getApple1 = input("Press the number of apples Consumer1 want to get: ")
#getOrange1 = input("Press the number of oranges Consumer1 want to get: ")
#getApple2 = input("Press the number of apples Consumer2 want to get: ")
#getOrange2 = input("Press the number of oranges Consumer2 want to get: ")
#print(f"Consumer1은 사과 {getApple1}개, 오렌지{getOrange1}개 입니다.")
#print(f"Consumer2은 사과 {getApple2}개, 오렌지{getOrange2}개 입니다.")


#---------------------------------------------------------------------------------


class Market:

    def __init__(self):
        # 마트에 있는 과일의 갯수
        self.__appleCount = 3
        self.__orangeCount = 5

    def casher(self):
        self.__getApple = int(input("Press the number of apples you want to get: "))
        self.__getOrange = int(input("Press the number of oranges you want to get: "))

        # 여기서 계산이 이루어져서 남은 과일의 갯수를 출력함
        self.__appleCount = int(self.__appleCount) - self.__getApple
        self.__orangeCount = int(self.__orangeCount) - self.__getOrange
        bill = [int(self.__appleCount), int(self.__orangeCount)]
        return print(f" 현재 저희 매장에 남은 과일의 갯수는: {bill}")

#Consumer1은 사과 1개 orange 3개
#Consumer2는 사과 2개, orange 1개

market = Market()
market.casher()
market.casher()