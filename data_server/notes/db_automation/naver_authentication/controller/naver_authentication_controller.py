from django.shortcuts import render
import uuid
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets, status

from account.service.account_service_impl import AccountServiceImpl
from account_profile.service.account_profile_service_impl import AccountProfileServiceImpl
from naver_authentication.service.naver_oauth_service_impl import NaverOauthServiceImpl
from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class NaverOauthController(viewsets.ViewSet):
    naverOauthService = NaverOauthServiceImpl.getInstance()
    accountService = AccountServiceImpl.getInstance()
    accountProfileService = AccountProfileServiceImpl.getInstance()
    redisCacheService = RedisCacheServiceImpl.getInstance()

    def requestAccessToken(self, request):
        code = request.GET.get('code')
        state = request.GET.get('state')

        if not code or not state:
            return JsonResponse({'error': 'code and state are required'}, status=400)

        print(f"[NAVER] Received code: {code}, state: {state}")

        try:
            tokenResponse = self.naverOauthService.requestAccessToken(code, state)
            accessToken = tokenResponse['access_token']
            print(f"accessToken: {accessToken}")

            with transaction.atomic():
                userInfo = self.naverOauthService.requestUserInfo(accessToken)
                print(f"userInfo: {userInfo}")

                response = userInfo.get('response', {})
                email = response.get('email', '')
                nickname = response.get('nickname', '')

                account = self.accountService.checkEmailDuplication(email)
                if account is None:
                    account = self.accountService.createAccount(email)
                    self.accountProfileService.createAccountProfile(
                        account.getId(), nickname
                    )

                userToken = self.__createUserTokenWithAccessToken(account, accessToken)
                # return JsonResponse({'userToken': userToken})

                return HttpResponse(f"""
                    <html>
                      <body>
                        <script>
                          const userToken = '{userToken}';
                          window.location.href = 'flutter://naver-login-success?userToken=' + userToken;
                        </script>
                      </body>
                    </html>
                """)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    def __createUserTokenWithAccessToken(self, account, accessToken):
        try:
            userToken = str(uuid.uuid4())
            self.redisCacheService.storeKeyValue(account.getId(), accessToken)
            self.redisCacheService.storeKeyValue(userToken, account.getId())
            return userToken
        except Exception as e:
            print('Redis에 토큰 저장 중 에러:', e)
            raise RuntimeError('Redis에 토큰 저장 중 에러')

