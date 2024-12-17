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
        #is_valid()는 객체에 포함된 데이터가 정의된 유효성 검사를 통과하는지 확인하는 메서드

        code = serializer.validated_data['code']
        #validated_data()는 검사를 통과한 후의 데이터이다
        #code값만 가져와 code에 넣는다

        try:
            accessToken = self.kakaoOauthService.requestAccessToken(code)
            print(f"accessToken: {accessToken}") #정상작동 하는지 보기위한 코드
            return JsonResponse({'accessToken': accessToken})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)