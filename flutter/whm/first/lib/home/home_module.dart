import 'package:first/home/presentation/ui/home_page.dart';
import 'package:first/kakao_authentication/presentation/providers/kakao_auth_providers.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';

import '../kakao_authentication/domain/usecase/login_usecase_impl.dart';
import '../kakao_authentication/infrasturcture/data_sources/kakao_auth_remote_data_source.dart';
import '../kakao_authentication/infrasturcture/repository/kakao_auth_repository.dart';
import '../kakao_authentication/infrasturcture/repository/kakao_auth_repository_impl.dart';

class HomeModule {
  static Widget provideHomePage() {
    dotenv.load();
    String baseServerUrl = dotenv.env['BASE_URL'] ?? '';

    return MultiProvider(
        providers: [
          Provider<KakaoAuthRemoteDataSource>(
              create: (_) => KakaoAuthRemoteDataSource(baseServerUrl)
          ),
          ProxyProvider<KakaoAuthRemoteDataSource, KakaoAuthRepository>(
            update: (_, remoteDataSrouce, __) =>
                KakaoAuthRepositoryImpl(remoteDataSrouce),
          ),
          ProxyProvider<KakaoAuthRepository, LoginUseCaseImpl>(
              update: (_, repository, __) =>
                  LoginUseCaseImpl(repository)
          ),
          ChangeNotifierProvider<KakaoAuthProvider>(
            create: (context) => KakaoAuthProvider(
              loginUseCase: context.read<LoginUseCaseImpl>(),
            ),
          ),
        ],
        child: HomePage()
    );
  }
}