import 'package:first/kakao_authentication/infrasturcture/data_sources/kakao_auth_remote_data_source.dart';
import 'package:kakao_flutter_sdk/kakao_flutter_sdk.dart';

import 'kakao_auth_repository.dart';

// class KakaoAuthRepositoryImpl(KakaoAuthRepository):
class KakaoAuthRepositoryImpl implements KakaoAuthRepository {
  final KakaoAuthRemoteDataSource remoteDataSource;

  KakaoAuthRepositoryImpl(this.remoteDataSource);

  // async는 비동기 처리를 지원함 (FastAPI에서 주로 봤었음)
  @override
  Future<String> login() async {
    print("KakaoAuthRepositoryImpl login()");
    return await remoteDataSource.loginWithKakao();
  }

  @override
  Future<User> fetchUserInfo() async {
    return await remoteDataSource.fetchUserInfoFromKakao();
  }
}