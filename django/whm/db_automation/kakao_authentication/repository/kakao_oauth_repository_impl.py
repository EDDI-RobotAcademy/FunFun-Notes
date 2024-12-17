import requests

from db_automation import settings
from kakao_authentication.repository.kakao_oauth_repository import KakaoOauthRepository


class KakaoOauthRepositoryImpl(KakaoOauthRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.loginUrl = settings.KAKAO['LOGIN_URL']
            cls.__instance.clientId = settings.KAKAO['CLIENT_ID']
            cls.__instance.redirectUri = settings.KAKAO['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.KAKAO['TOKEN_REQUEST_URI']
            cls.__instance.userInfoRequestUri = settings.KAKAO['USER_INFO_REQUEST_URI']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def getOauthLink(self):
        print("getOauthLink() for Login")
        #디버깅용으로 확인을 위한 메세지 출력코드

        return (f"{self.loginUrl}/oauth/authorize?" 
                f"client_id={self.clientId}&redirect_uri={self.redirectUri}&response_type=code")
    # https://kauth.kakao.com/oauth/authorize?client_id=YOUR_CLIENT_ID&redirect_uri=YOUR_REDIRECT_URI&response_type=code
    #출력된다

    def getAccessToken(self, code):
        accessTokenRequest = {
            'grant_type': 'authorization_code',
            #authorization_code는 인증코드를 사용하요 액세스 토큰을 얻는 방식이다

            'client_id': self.clientId,
            'redirect_uri': self.redirectUri,
            #setting.py를 통해 .env를 통해 가져온다
            'code': code,
            #controller에서 얻은 코드값
            'client_secret': None
        }

        response = requests.post(self.tokenRequestUri, data=accessTokenRequest)
        return response.json()