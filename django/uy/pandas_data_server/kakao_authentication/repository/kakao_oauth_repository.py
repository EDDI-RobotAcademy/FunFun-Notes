from abc import ABC, abstractmethod


class KakaoOauthRepository(ABC):

    @abstractmethod
    def getOauthLink(self):
        pass

    @abstractmethod
    def getAccessToken(self, code):
        pass