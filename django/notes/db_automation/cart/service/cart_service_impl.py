from django.db.models import OuterRef, Subquery, Value
from django.db.models.functions import Coalesce
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from account.repository.account_repository_impl import AccountRepositoryImpl
from cart.entity.cart import Cart
from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.service.cart_service import CartService
from game_software.entity.game_software import GameSoftware
from game_software.entity.game_software_image import GameSoftwareImage
from game_software.entity.game_software_price import GameSoftwarePrice
from game_software.repository.game_software_repository_impl import GameSoftwareRepositoryImpl


class CartServiceImpl(CartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__cartRepository = CartRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__gameSoftwareRepository = GameSoftwareRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createCart(self, accountId, cart):
        foundAccount = self.__accountRepository.findById(accountId)

        if not foundAccount:
            raise Exception("해당 accountId에 해당하는 account를 찾을 수 없습니다.")

        foundGameSoftware = self.__gameSoftwareRepository.findById(cart["id"])

        if not foundGameSoftware:
            raise Exception("해당 gameSoftwareId에 해당하는 게임을 찾을 수 없습니다.")

        foundCart = self.__cartRepository.findCartByAccountAndGameSoftware(foundAccount, foundGameSoftware)

        if foundCart:
            foundCart.quantity += cart["quantity"]
            updatedCart = self.__cartRepository.save(foundCart)
            return updatedCart

        newCart = Cart(
            account=foundAccount,
            gameSoftware=foundGameSoftware,
            quantity=cart["quantity"]
        )
        savedCart = self.__cartRepository.save(newCart)
        return savedCart

    def listCart(self, accountId, page, pageSize):
        try:
            print(f"listCart() pageSize: {pageSize}")

            # Account 확인
            account = self.__accountRepository.findById(accountId)
            if not account:
                raise ValueError(f"Account with ID {accountId} not found.")
            print(f"Account found: {account}")

            # Offset 및 Limit 계산
            offset = (page - 1) * pageSize
            limit = pageSize
            print(f"Offset: {offset}, Limit: {limit}")

            # Cart 목록 가져오기
            cartListQuery = self.__cartRepository.findCartByAccount(account, offset, limit)
            print(f"Cart list query retrieved: {cartListQuery}")

            # 가격 및 이미지 서브쿼리를 Cart에 맞게 연결
            annotatedCartList = cartListQuery.annotate(
                price=Coalesce(
                    Subquery(
                        GameSoftwarePrice.objects.filter(
                            gameSoftware=OuterRef("gameSoftware")
                        ).values("price")[:1]
                    ),
                    Value(0),
                ),
                image=Coalesce(
                    Subquery(
                        GameSoftwareImage.objects.filter(
                            gameSoftware=OuterRef("gameSoftware")
                        ).values("image")[:1]
                    ),
                    Value(""),
                ),
            )
            print(f"Annotated cart list: {annotatedCartList}")

            # Paginator로 페이지네이션 적용
            paginator = Paginator(annotatedCartList, pageSize)
            try:
                paginatedCartList = paginator.page(page)
            except PageNotAnInteger:
                paginatedCartList = paginator.page(1)
            except EmptyPage:
                paginatedCartList = []

            # 필요한 데이터만 추출
            cartDataList = [
                {
                    "id": cart.id,
                    "title": cart.gameSoftware.title,
                    "price": cart.price,
                    "image": cart.image,
                    "quantity": cart.quantity,
                }
                for cart in paginatedCartList
            ]

            print(f"Total items: {paginator.count}")
            print(f"Page items: {len(cartDataList)}")

            return cartDataList, paginator.num_pages

        except Exception as e:
            print(f"Unexpected error in listCart: {e}")
            raise
    