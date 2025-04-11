import 'package:first/home/home_module.dart';
import 'package:first/kakao_authentication/domain/usecase/login_usecase_impl.dart';
import 'package:first/kakao_authentication/infrasturcture/data_sources/kakao_auth_remote_data_source.dart';
import 'package:first/kakao_authentication/infrasturcture/repository/kakao_auth_repository.dart';
import 'package:first/kakao_authentication/infrasturcture/repository/kakao_auth_repository_impl.dart';
import 'package:flutter/material.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:kakao_flutter_sdk/kakao_flutter_sdk.dart';
import 'package:provider/provider.dart';

import 'authentication/presentation/ui/login_page.dart';
import 'base_url_provider.dart';
import 'home/presentation/ui/home_page.dart';
import 'kakao_authentication/domain/usecase/fetch_user_info_usecase_impl.dart';
import 'kakao_authentication/domain/usecase/request_user_token_usecase_impl.dart';

import 'package:flutter_localizations/flutter_localizations.dart';
import 'package:flutter_quill/flutter_quill.dart' as quill;

import 'kakao_authentication/presentation/providers/kakao_auth_providers.dart';
import 'main_module.dart';

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
    print("baseUrl: $baseUrl");

    return MultiProvider(
        providers: [
          // BaseUrlProvider를 Consumer로 감싸서 baseUrl을 처리
          ChangeNotifierProvider<BaseUrlProvider>(
            create: (_) => BaseUrlProvider(baseUrl),
          ),
          ...MainModule.provideAppModules(),  // MainModule에서 제공하는 인증 관련 모듈들
        ],
      child: MaterialApp(
        title: 'Flutter Demo',
        theme: ThemeData(
          colorScheme: ColorScheme.fromSeed(seedColor: Colors.deepPurple),
          useMaterial3: true,
        ),
        localizationsDelegates: [
          GlobalMaterialLocalizations.delegate,
          GlobalWidgetsLocalizations.delegate,
          quill.FlutterQuillLocalizations.delegate, // Add this line to fix the error
        ],
        supportedLocales: [
          Locale('en', 'US'), // Add supported locales
          Locale('ko', 'KR'), // For example, support Korean
        ],
        // home: HomeModule.provideHomePage(loginType: "Kakao"),
        home: Consumer<KakaoAuthProvider>(
          builder: (context, kakaoProvider, child) {
            if (kakaoProvider.isLoggedIn) {
              return HomePage(loginType: "Kakao");
            } else {
              return LoginPage();
            }
          },
        ),
      )
    );
  }
}

