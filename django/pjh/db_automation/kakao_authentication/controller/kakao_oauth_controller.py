from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

from kakao_authentication.serializer.kakao_oauth_access_token_serializer import KakaoOauthAccessTokenSerializer
from kakao_authentication.service.kakao_oauth_service_impl import KakaoOauthServiceImpl


class KakaoOauthController(viewsets.ViewSet):
    kakaoOauthService = KakaoOauthServiceImpl.getInstance()

    def requestKakaoOauthLink(self, request):
        url = self.kakaoOauthService.requestKakaoOauthLink()

        return JsonResponse({"url": url}, status=status.HTTP_200_OK)

    def requestAccessToken(self, request):
        serializer = KakaoOauthAccessTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data['code']

        try:
            accessToken = self.kakaoOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}")
            return JsonResponse({'accessToken': accessToken})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
