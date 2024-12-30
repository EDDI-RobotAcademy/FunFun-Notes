from account.repository.account_repository_impl import AccountRepositoryImpl
from cart.entity.cart import Cart
from cart.repository.cart_repository_impl import CartRepositoryImpl
from cart.service.cart_service import CartService
from game_software.repository.game_software_repository import GameSoftwareRepository
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
    