from abc import ABC, abstractmethod


class RedisCacheService(ABC):
    @abstractmethod
    def storeAccessToken(self, account_id, userToken):
        pass

    @abstractmethod
    def getValueByKey(self, key):
        pass

    @abstractmethod
    def deleteKey(self, key):
        pass
