import 'package:first/kakao_authentication/domain/usecase/login_usecase.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import '../../domain/usecase/fetch_user_info_usecase.dart';

class KakaoAuthProvider with ChangeNotifier {
  final LoginUseCase loginUseCase;
  final FetchUserInfoUseCase fetchUserInfoUseCase;

  final FlutterSecureStorage secureStorage = FlutterSecureStorage();

  String? _accessToken;
  bool _isLoggedIn = false;
  bool _isLoading = false;
  String _message = '';

  // 해당 변수 값을 즉시 가져올 수 있도록 구성
  bool get isLoggedIn => _isLoggedIn;
  bool get isLoading => _isLoading;
  String get message => _message;

  KakaoAuthProvider({
    required this.loginUseCase,
    required this.fetchUserInfoUseCase,
  });

  Future<void> login() async {
    _isLoading = true;
    _message = '';
    notifyListeners();

    try {
      print("Kakao loginUseCase.execute()");
      _accessToken = await loginUseCase.execute();
      print("AccessToken obtained: $_accessToken");

      final userInfo = await fetchUserInfoUseCase.execute();
      print("User Info fetched: $userInfo");

      final email = userInfo.kakaoAccount?.email;
      final nickname = userInfo.kakaoAccount?.profile?.nickname;

      print("User email: $email, User nickname: $nickname");
    } catch (e) {
      _isLoggedIn = false;
      _message = "로그인 실패: $e";
    }

    _isLoading = false;
    notifyListeners();
  }
}