import 'package:first/home/home_module.dart';
import 'package:first/kakao_authentication/domain/usecase/login_usecase_impl.dart';
import 'package:first/kakao_authentication/infrasturcture/data_sources/kakao_auth_remote_data_source.dart';
import 'package:first/kakao_authentication/infrasturcture/repository/kakao_auth_repository.dart';
import 'package:first/kakao_authentication/infrasturcture/repository/kakao_auth_repository_impl.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:kakao_flutter_sdk/kakao_flutter_sdk.dart';
import 'package:provider/provider.dart';

import 'home/presentation/ui/home_page.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await dotenv.load();

  String baseServerUrl = dotenv.env['BASE_URL'] ?? '';
  String kakaoNativeAppKey = dotenv.env['KAKAO_NATIVE_APP_KEY'] ?? '';
  String kakaoJavaScriptAppKey = dotenv.env['KAKAO_JAVASCRIPT_APP_KEY'] ?? '';

  KakaoSdk.init(
    nativeAppKey: kakaoNativeAppKey,
    javaScriptAppKey: kakaoJavaScriptAppKey,
  );

  runApp(MyApp(baseUrl: baseServerUrl));
}

class MyApp extends StatelessWidget {
  final String baseUrl;

  const MyApp({required this.baseUrl});

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
        providers: [
          Provider<KakaoAuthRemoteDataSource>(
              create: (_) => KakaoAuthRemoteDataSource(baseUrl)
          ),
          ProxyProvider<KakaoAuthRemoteDataSource, KakaoAuthRepository>(
            update: (_, remoteDataSrouce, __) =>
                KakaoAuthRepositoryImpl(remoteDataSrouce),
          ),
          ProxyProvider<KakaoAuthRepository, LoginUseCaseImpl>(
              update: (_, repository, __) =>
                  LoginUseCaseImpl(repository)
          ),
        ],
        child: MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(
            colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
            useMaterial3: true,
          ),
          home: HomeModule.provideHomePage(),
        )
    );
  }
}
