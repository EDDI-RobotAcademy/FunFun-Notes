
class Mart:
    def __init__(self, apple_stock, orange_stock):
        self.num_apple = apple_stock
        self.num_orange = orange_stock
        self.items = ["사과", "오렌지"]

    def check_stock(self, fruit, order_num):
        if fruit == "사과":
            if order_num > self.num_apple:
                print(f"재고가 부족합니다. 현재 남은 갯수 {self.num_apple}개")
                return False
            else:
                self.num_apple -= order_num
                print(f"사과 {order_num}개 구매하셨습니다. 현재 남은 갯수 {self.num_apple}개")
                return True

        elif fruit == "오렌지":
            if order_num > self.num_orange:
                print(f"재고가 부족합니다. 현재 남은 갯수 {self.num_orange}개")
                return False
            else:
                self.num_orange -= order_num
                print(f"오렌지 {order_num}개 구매하셨습니다. 현재 남은 갯수 {self.num_orange}개")
                return True


    def remain_stock(self):
        print(f"남은 사과: {self.num_apple}개, 남은 오렌지: {self.num_orange}개")


    def order(self):
        while True:
            order_fruit = input("무슨 과일을 구매하시나요?: ")
            if order_fruit not in self.items:
                print(f"해당 상품이 없습니다. 현재 재고 종류: {', '.join(self.items)}")
                continue
            order_num = int(input("몇 개 구매하시나요?: "))
            if self.check_stock(order_fruit, order_num):
                self.remain_stock()

            order_again = input("주문을 계속 하시겠습니까? (y/n): ")
            if order_again != "y":
                print("주문을 종료합니다.")
                break

fruits = Mart(apple_stock=3, orange_stock=5)
fruits.order()
