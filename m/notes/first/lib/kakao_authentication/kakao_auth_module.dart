import 'package:first/kakao_authentication/presentation/providers/kakao_auth_providers.dart';
import 'package:first/kakao_authentication/presentation/ui/kakao_login_page.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';
import 'package:provider/single_child_widget.dart';

import 'domain/usecase/fetch_user_info_usecase_impl.dart';
import 'domain/usecase/login_usecase_impl.dart';
import 'domain/usecase/request_user_token_usecase_impl.dart';
import 'infrasturcture/data_sources/kakao_auth_remote_data_source.dart';
import 'infrasturcture/repository/kakao_auth_repository.dart';
import 'infrasturcture/repository/kakao_auth_repository_impl.dart';

class KakaoAuthModule {
  static List<SingleChildWidget> provideKakaoProviders(String baseUrl) {
    print("baseUrl: $baseUrl");

    return [
      Provider<KakaoAuthRemoteDataSource>(
        create: (_) => KakaoAuthRemoteDataSource(baseUrl),
      ),
      ProxyProvider<KakaoAuthRemoteDataSource, KakaoAuthRepository>(
        update: (_, remoteDataSource, __) =>
            KakaoAuthRepositoryImpl(remoteDataSource),
      ),
      ProxyProvider<KakaoAuthRepository, LoginUseCaseImpl>(
        update: (_, repository, __) =>
            LoginUseCaseImpl(repository),
      ),
      ProxyProvider<KakaoAuthRepository, FetchUserInfoUseCaseImpl>(
        update: (_, repository, __) =>
            FetchUserInfoUseCaseImpl(repository),
      ),
      ProxyProvider<KakaoAuthRepository, RequestUserTokenUseCaseImpl>(
        update: (_, repository, __) =>
            RequestUserTokenUseCaseImpl(repository),
      ),
      ChangeNotifierProvider<KakaoAuthProvider>(
        create: (context) => KakaoAuthProvider(
          loginUseCase: context.read<LoginUseCaseImpl>(),
          fetchUserInfoUseCase: context.read<FetchUserInfoUseCaseImpl>(),
          requestUserTokenUseCase: context.read<RequestUserTokenUseCaseImpl>(),
        ),
      ),
    ];
  }

  static Widget provideKakaoLoginPage() {
    return KakaoLoginPage();
  }
}
