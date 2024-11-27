class Mart:
    def __init__(self):
        self.fruits = {}

    def add_fruit(self, fruit):
        """마트에 과일 추가"""
        self.fruits[fruit.name] = fruit

    def remove_fruit(self, name):
        """마트에서 과일 제거"""
        if name in self.fruits:
            del self.fruits[name]
        else:
            print(f"{name}는 마트에 없습니다.")

    def get_fruits(self):
        """마트의 과일 목록 반환"""
        return self.fruits

    def update_fruit(self, name, count):
        """마트의 과일 수량 업데이트"""
        if name in self.fruits:
            self.fruits[name].count = count
        else:
            print(f"{name}는 마트에 없습니다.")