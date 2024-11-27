def main():
    # 마트 생성 및 과일 추가
    mart = Mart()
    apple = Fruit("사과", 10)
    banana = Fruit("바나나", 5)
    mart.add_fruit(apple)
    mart.add_fruit(banana)

    customer = Customer()

    while True:
        # 과일 목록 출력
        print("현재 마트에 있는 과일 목록:")
        for name, fruit in mart.fruits.items():
            print(f"{name}: {fruit.count}개")

        # 과일 추가 또는 주문 여부 결정
        choice = input("주문을 하시겠습니까? (예/아니오) 또는 과일을 추가하시겠습니까? (추가/삭제/업데이트): ")

        if choice.lower() == '예':
            while True:
                # 주문할 과일 목록 출력
                print("주문 가능한 과일 목록:")
                for name, fruit in mart.fruits.items():
                    print(f"{name}: {fruit.count}개")

                # 주문할 과일 이름 입력
                order_fruit = input("주문할 과일 이름을 입력하세요 (종료하려면 'q'를 입력하세요): ")
                if order_fruit == 'q':
                    break

                # 주문할 과일 수량 입력
                try:
                    order_amount = int(input(f"{order_fruit}의 수량을 입력하세요: "))
                except ValueError:
                    print("잘못된 입력입니다. 다시 시도해주세요.")
                    continue

                # 주문 처리
                if order_fruit in mart.fruits and mart.fruits[order_fruit].count >= order_amount:
                    mart.fruits[order_fruit].decrease_count(order_amount)
                    customer.order_fruit(order_fruit, order_amount)
                else:
                    print(f"{order_fruit}는 재고가 부족하여 {order_amount}개 구매할 수 없습니다.")

            # 주문 결과 출력
            print("\n주문 결과:")
            customer.show_order_result()
            print("\n고객이 주문한 과일 목록:")
            for name, amount in customer.orders:
                print(f"{name}: {amount}개")

        elif choice.lower() == '추가':
            while True:
                # 추가할 과일 이름 입력
                add_fruit = input("추가할 과일 이름을 입력하세요 (종료하려면 'q'를 입력하세요): ")
                if add_fruit == 'q':
                    break

                # 추가할 과일 수량 입력
                try:
                    add_amount = int(input(f"{add_fruit}의 수량을 입력하세요: "))
                except ValueError:
                    print("잘못된 입력입니다. 다시 시도해주세요.")
                    continue

                # 과일 추가
                # if add_fruit not in mart.fruits:
                #     print(f"{add_fruit}는 마트에 없습니다. 다시 입력해주세요.")
                else:
                    mart.add_fruit(Fruit(add_fruit, add_amount))
                    customer.order_fruit(add_fruit, add_amount)

        elif choice.lower() == '삭제':
            # 삭제할 과일 이름 입력
            delete_fruit = input("삭제할 과일 이름을 입력하세요 (종료하려면 'q'를 입력하세요): ")
            if delete_fruit == 'q':
                break
            mart.remove_fruit(delete_fruit)

        elif choice.lower() == '업데이트':
            # 업데이트할 과일 이름과 수량 입력
            update_fruit = input("업데이트할 과일 이름과 수량을 입력하세요 (종료하려면 'q'를 입력하세요): ")
            if update_fruit == 'q':
                break
            name, count = update_fruit.split()
            count = int(count)
            mart.update_fruit(name, count)

        else:
            print("고객이 주문한 과일 목록:")
            for name, amount in customer.orders:
                print(f"{name}: {amount}개")
            print("현재 마트에 있는 과일 목록:")
            for name, fruit in mart.fruits.items():
                print(f"{name}: {fruit.count}개")
            break

if __name__ == "__main__":
    main()
