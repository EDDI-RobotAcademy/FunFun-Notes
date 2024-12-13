from abc import ABC, abstractmethod


class KakaoOauthService(ABC):

    @abstractmethod
    def requestKakaoOauthLink(self):
        pass