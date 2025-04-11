from abc import ABC, abstractmethod

class NaverOauthRepository(ABC):

    @abstractmethod
    def getAccessToken(self, code, state):
        pass

    @abstractmethod
    def getUserInfo(self, accessToken):
        pass
