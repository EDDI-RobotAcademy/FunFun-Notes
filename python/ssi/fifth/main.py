class Mart:
    def __init__(self):
        self.inventory = {
            "Apple" : 3,
            "Orange" : 5,
            "Pear" : 0
        }
    
    def get_item_qunatity(self, item):
        if item not in self.inventory:
            return None
        return self.inventory[item.capitalize()]

    def display_inventory(self):
        print("\n현재 마트 재고 : ")
        for item, quantity in self.inventory.items():
            print(f"{item.capitalize()} : {quantity}개")
        print()

    def sell_item(self, items):
        for item, quantity in items.items():
            if item not in self.inventory:
                print("죄송합니다. {item}은(는) 마트에 없습니다")
                continue

            if self.inventory[item] >= quantity:
                self.inventory[item] -= quantity
                print(f"{item.capitalize()} {quantity}개를 판매했습니다")
            
            else:
                print(f"죄송합니다 {item}의 재고가  없습니다. 현재 재고 {self.inventory[item]}개")

    def add_stock(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
            print(f"{item.capitalize()} {quantity}개를 재고에 추가했습니다")
        else:
            print(f"죄송합니다. {item}은(는) 존재하지 않습니다. 먼저 물품을 추가해주세요")

    def add_new_item(self, item, quantity):
        if item in self.inventory:
            print(f"{item.capitalize()}은(는) 이미 존재합니다. 기존 재고를 사용해 주세요")
        else:
            self.inventory[item] = quantity
            print(f"{item.capitalize()} {quantity}개를 새롭게 추가했습니다.")


def main():
    mart = Mart()

    while True:
        print("\n-----------------마트 관리 시스템-----------------")
        print("1. 현재 재고 확인")
        print("2. 물품 판매")
        print("3. 재고 추가")
        print("4. 물품 추가")
        print("5. 종료")

        choice = input("원하는 작업을 입력하세요(1~5) : ")

        if choice == "1":
            mart.display_inventory()
        
        elif choice == "2":
            mart.display_inventory()
            item_to_buy = {}

            print("구매할 물품과 수량을 입력해주세요. (예 : apple 2)")

            try:
                item, quantity = input("> ").split()
                quantity = int(quantity)
                print(f"물품 : {item}, 수량 : {quantity}")

                if quantity < 0:
                    print("구매하고자 하는 수량은 0보다 커야 합니다")
                    continue
                available_quantity = mart.get_item_qunatity(item.capitalize())
                if available_quantity is None:
                    print(f"죄송합니다. {item}은(는) 마트에 없습니다.")
                    continue

                if available_quantity < quantity:
                    print(f"죄송합니다. 현재 {item}의 재고가 부족합니다. 현재 재고 : {available_quantity}개")
                
                item_to_buy[item.capitalize()] = quantity
            
            except ValueError:
                print("올바른 형식으로 입력하세요. (예 : apple 2)")

            mart.sell_item(item_to_buy)

        elif choice == "3": #재고 추가
            print("재고를 추가할 물품과 수량을 입력하세요. (예 : apple 5)")

            try:
                item, quantity = input("> ").split()
                quantity = int(quantity)

                if quantity < 0:
                    print("추가하고자 하는 수량은 0 이상이어야 합니다")
                    continue
                mart.add_stock(item.capitalize(), quantity)

            except ValueError:
                print("올바른 형식으로 입력하세요. (예 : apple 5)")

            mart.display_inventory()

        elif choice == "4": #물품 추가
            print("추가할 물품과 수량을 입력해주세요. (예 : banana 10)")

            try:
                item, quantity = input("> ").split()
                quantity = int(quantity)

                if quantity < 0:
                    print("수량은 0 보다 커야합니다.")
                    continue
                mart.add_new_item(item.capitalize(), quantity)

            except ValueError:
                print("올바른 형식으로 입력하세요. (예 : banana 10)")

            mart.display_inventory()

        elif choice == "5": #종료
            print("마트 시스템을 종료합니다.")
            break
        else:
            print("올바른 선택지를 입력하세요. (1~5)")

if __name__ == "__main__":
    main()

