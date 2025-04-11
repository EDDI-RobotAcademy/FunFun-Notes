import 'package:provider/provider.dart';
import 'package:provider/single_child_widget.dart';

import 'package:first/kakao_authentication/kakao_auth_module.dart';

import 'base_url_provider.dart';
// 이후 추가될 모듈
// import 'package:first/naver_authentication/naver_auth_module.dart';
// import 'package:first/meta_authentication/meta_auth_module.dart';
// import 'package:first/google_authentication/google_auth_module.dart';

class MainModule {
  static List<SingleChildWidget> provideAppModules() {
    return [
      Consumer<BaseUrlProvider>(
        builder: (context, baseUrlProvider, child) {
          String baseUrl = baseUrlProvider.baseUrl;

          // 각 인증 모듈에서 baseUrl을 사용하는 방식으로 수정
          return MultiProvider(
            providers: [
              ...KakaoAuthModule.provideKakaoProviders(baseUrl),
              // 다른 인증 모듈들도 동일한 방식으로 추가
              // ...NaverAuthModule.provideNaverProviders(baseUrl),
              // ...MetaAuthModule.provideMetaProviders(baseUrl),
              // ...GoogleAuthModule.provideGoogleProviders(baseUrl),
            ],
            child: child!,
          );
        },
      ),
    ];
  }
}
