class Customer:
    def __init__(self):
        self.orders = []

    def order_fruit(self, name, amount):
        """과일 주문"""
        self.orders.append((name, amount))

    def show_order_result(self):
        """주문 결과 출력"""
        print("주문 내역:")
        for name, amount in self.orders:
            print(f"{name}: {amount}개")