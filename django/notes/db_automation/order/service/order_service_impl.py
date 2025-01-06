from django.db import transaction

from account.repository.account_repository_impl import AccountRepositoryImpl
from cart.repository.cart_repository_impl import CartRepositoryImpl
from game_software.repository.game_software_price_repository_impl import GameSoftwarePriceRepositoryImpl
from game_software.repository.game_software_repository_impl import GameSoftwareRepositoryImpl
from order.entity.orders import Order
from order.entity.order_items import OrderItems
from order.entity.order_status import OrderStatus
from order.repository.order_item_repository_impl import OrderItemRepositoryImpl
from order.repository.order_repository_impl import OrderRepositoryImpl
from order.service.order_service import OrderService


class OrderServiceImpl(OrderService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__orderItemRepository = OrderItemRepositoryImpl.getInstance()
            cls.__instance.__gameSoftwareRepository = GameSoftwareRepositoryImpl.getInstance()
            cls.__instance.__gameSoftwarePriceRepository = GameSoftwarePriceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    @transaction.atomic
    def createOrder(self, accountId, items, total):
        account = self.__accountRepository.findById(accountId)

        if not account:
            raise Exception(f"Account id {accountId} 존재하지 않음.")

        # 2. 총 금액 검증
        if not isinstance(total, (int, float)) or total <= 0:
            raise Exception("유효하지 않은 총 금액입니다.")

        # 3. 주문 항목 검증
        if not items or not isinstance(items, list):
            raise Exception("유효하지 않은 주문 항목입니다.")

        orders = Order(
            account=account,
            total_amount=total,
            status=OrderStatus.PENDING,
        )
        orders = self.__orderRepository.save(orders)
        print(f"order 생성")

        orderItemList = []

        for item in items:
            cartItem = self.__cartRepository.findById(item["id"])
            if not cartItem:
                raise Exception(f"Cart item ID {item['id']} 존재하지 않음.")
            if item["quantity"] <= 0:
                raise Exception(f"Cart item ID {item['id']}의 수량이 유효하지 않음.")

            # 5. 게임 소프트웨어 가격 확인
            gameSoftware = cartItem.getGameSoftware()
            if not gameSoftware:
                raise Exception(f"Game software with ID {gameSoftware.getId()} 존재하지 않음.")

            gameSoftwarePrice = self.__gameSoftwarePriceRepository.findByGameSoftware(gameSoftware)

            # 6. 주문 항목 객체 생성
            orderItem = OrderItems(
                orders=orders,
                game_software=gameSoftware,
                quantity=item["quantity"],
                price=gameSoftwarePrice.getPrice() * item["quantity"],  # 총 가격은 게임 소프트웨어의 가격과 수량의 곱
            )
            orderItemList.append(orderItem)
            print(f"orderItemList: {orderItemList}")
            
            print(f"orderItem 생성")

        if orderItemList:
            self.__orderItemRepository.bulkCreate(orderItemList)

        return orders.getId()