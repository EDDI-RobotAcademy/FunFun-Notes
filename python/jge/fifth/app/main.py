#1. 마트에 사과 3개가 있다.
#2. 마트에 오렌지가 5개 있다.
#3. 구매자가 와서 사과와 배를 사갔다.
#->과일 종류, 갯수 인풋 받아서 마트에 몇개 남았는지 프린트
#DDD가 어렵다면 통 main으로 만들어도 무방합니다.
# 단순하게 선언?

num_apple = 3
num_orange = 5

while True:
    order_fruit = input("무슨 과일을 구매하시나요?: ")
    order_num = int(input("몇 개 구매하시나요?: "))
    if order_fruit == "사과":
        if order_num > num_apple:
            print(f"재고가 부족합니다. 현재 남은 갯수 {num_apple}개")
        else:
            num_apple -= order_num
            print(f"사과 {order_num}개 구매하셨습니다. 현재 남은 갯수 {num_apple}개")

    elif order_fruit == "오렌지":
        if order_num > num_orange:
            print(f"재고가 부족합니다. 현재 남은 갯수 {num_orange}개")
        else:
            num_orange -= order_num
            print(f"오렌지 {order_num}개 구매하셨습니다. 현재 남은 갯수 {num_orange}개")

    print(f"남은 사과: {num_apple}개, 남은 오렌지: {num_orange}개")

    order_again = input("주문을 계속 하시겠습니까? (y/n): ")
    if order_again != "y":
        print("주문을 종료합니다.")
        break





















