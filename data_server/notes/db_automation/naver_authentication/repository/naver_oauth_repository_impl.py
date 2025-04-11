import requests
from django.conf import settings

class NaverOauthRepositoryImpl:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.loginUrl = settings.NAVER['LOGIN_URL']
            cls.__instance.clientId = settings.NAVER['CLIENT_ID']
            cls.__instance.clientSecret = settings.NAVER['CLIENT_SECRET']
            cls.__instance.redirectUri = settings.NAVER['REDIRECT_URI']
            cls.__instance.tokenRequestUri = settings.NAVER['TOKEN_REQUEST_URI']
            cls.__instance.userInfoRequestUri = settings.NAVER['USER_INFO_REQUEST_URI']

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def getOauthLink(self):
        print("getOauthLink() for Naver Login")
        return (
            f"{self.loginUrl}?"
            f"client_id={self.clientId}&response_type=code&"
            f"redirect_uri={self.redirectUri}&state=random_state"
        )

    def getAccessToken(self, code, state):
        print("getAccessToken() for Naver Login")
        params = {
            'grant_type': 'authorization_code',
            'client_id': self.clientId,
            'client_secret': self.clientSecret,
            'code': code,
            'state': state
        }

        print(f"tokenRequestUri: {self.tokenRequestUri}")

        response = requests.get(self.tokenRequestUri, params=params)
        response.raise_for_status()
        return response.json()

    def getUserInfo(self, accessToken):
        print("getUserInfo() for Naver Login")
        headers = {
            'Authorization': f'Bearer {accessToken}'
        }

        response = requests.get(self.userInfoRequestUri, headers=headers)
        response.raise_for_status()
        return response.json()
