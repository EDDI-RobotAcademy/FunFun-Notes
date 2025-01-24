import 'package:kakao_flutter_sdk/kakao_flutter_sdk.dart';

class KakaoAuthRemoteDataSource {
  final String baseUrl;

  KakaoAuthRemoteDataSource(this.baseUrl);

  Future<String> loginWithKakao() async {
    try {
      OAuthToken token;
      if (await isKakaoTalkInstalled()) {
        token = await UserApi.instance.loginWithKakaoTalk();
        print('카카오톡으로 로그인 성공: ${token.accessToken}');
      } else {
        token = await UserApi.instance.loginWithKakaoAccount();
        print('카카오 계정으로 로그인 성공: ${token.accessToken}');
      }

      return token.accessToken;
    } catch (error) {
      print("로그인 실패: $error");
      throw Exception("Kakao 로그인 실패!");
    }
  }
}