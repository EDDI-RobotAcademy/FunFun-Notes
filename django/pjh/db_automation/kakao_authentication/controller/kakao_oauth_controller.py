from django.http import JsonResponse
from rest_framework import viewsets, status

from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl


class KakaoOauthController(viewsets.ViewSet):
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()

    def requestKakaoOauthLink(self, request):
        url = self.kakaoOauthService.requestKakaoOauthLink()

        return JsonResponse({"url": url}, status=status.HTTP_200_OK)
