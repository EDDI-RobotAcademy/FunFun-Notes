class Fruit:
    def __init__(self, name, count):
        self.name = name
        self.count = count

    def decrease_count(self, amount):
        """과일 수량 감소"""
        if self.count >= amount:
            self.count -= amount
        else:
            print(f"{self.name}는 재고가 부족하여 {amount}개 구매할 수 없습니다.")

    def restock(self, supplement):
        """재고 보충"""
        if supplement > 0:
            self.count += supplement
        else:
            print("재고 보충량은 양수여야 합니다.")