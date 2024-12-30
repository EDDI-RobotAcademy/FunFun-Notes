from cart.entity.cart import Cart
from cart.repository.cart_repository import CartRepository


class CartRepositoryImpl(CartRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def save(self, cart):
        try:
            if cart.getId():
                existingCart = Cart.objects.get(id=cart.id)
                existingCart.quantity = cart.quantity  # 수량 업데이트
                existingCart.save()
                return existingCart

            new_cart = Cart.objects.create(
                account=cart.account,
                gameSoftware=cart.gameSoftware,
                quantity=cart.quantity
            )
            return new_cart
        except Exception as e:
            print(f"장바구니 저장 중 오류 발생: {e}")
            raise

    def findCartByAccountAndGameSoftware(self, account, gameSoftware):
        try:
            cart = Cart.objects.get(account=account, gameSoftware=gameSoftware)
            return cart

        except Cart.DoesNotExist:
            return None

        except Cart.MultipleObjectsReturned:
            print("오류: 조건에 만족하는 장바구니가 여러 개 존재합니다.")
            return None

        except Exception as e:
            print(f"장바구니 조회 중 오류 발생: {e}")
            return None
