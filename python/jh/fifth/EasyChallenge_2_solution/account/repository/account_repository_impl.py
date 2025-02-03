from account.entity.account import Account
from account.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    __instance = None

    __accountList = []
    __currentSignInUserId = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getCurrentSignInUserId(self):
        return self.__currentSignInUserId

    def register(self, accountId, password):
        account = Account(accountId, password)
        self.__accountList.append(account)

    def login(self, accountId, password):
        maybeAccount = self.findByAccountId(accountId)
        if maybeAccount is None:
            return False

        if maybeAccount.getPassword() != password:
            return False

        self.__currentSignInUserId = maybeAccount.getId()
        return True

    def findByAccountId(self, accountId):
        for account in self.__accountList:
            if account.getAccountId() == accountId:
                return account

        return None

    def findById(self, id):
        for account in self.__accountList:
            if account.getId() == id:
                return account

        return None
