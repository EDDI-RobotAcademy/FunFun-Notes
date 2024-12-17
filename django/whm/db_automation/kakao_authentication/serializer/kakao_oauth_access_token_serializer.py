from rest_framework import serializers

class KakaoOauthAccessTokenSerializer(serializers.Serializer):
    code = serializers.CharField()
    #인가를 위한 카카오사의 코드값