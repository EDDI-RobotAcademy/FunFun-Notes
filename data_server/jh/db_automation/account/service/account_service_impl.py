from django.core.exceptions import ObjectDoesNotExist

from account.repository.account_repository_impl import AccountRepositoryImpl
from account.service.account_service import AccountService


class AccountServiceImpl(AccountService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def createAccount(self, email):
        print("AAA0")
        return self.__accountRepository.save(email)

    def createAdminAccount(self, email):
        return self.__accountRepository.saveAdmin(email)

    def checkEmailDuplication(self, email):
        try:
            print("AAA1")
            return self.__accountRepository.findByEmail(email)

        except ObjectDoesNotExist:
            return None

    def findEmail(self, accountId):
        try:
            print("AAA2")
            account = self.__accountRepository.findById(accountId)
            if account:
                return account.getEmail()  # account 객체에서 이메일 반환
            return None  # 이메일이 없으면 None 반환

        except ObjectDoesNotExist:
            return None