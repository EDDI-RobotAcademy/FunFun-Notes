from abc import ABC, abstractmethod

class NaverOauthService(ABC):

    @abstractmethod
    def requestAccessToken(self, code, state):
        pass

    @abstractmethod
    def requestUserInfo(self, accessToken):
        pass
