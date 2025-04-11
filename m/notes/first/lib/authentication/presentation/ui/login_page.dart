import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../../home/home_module.dart';
import '../../../kakao_authentication/presentation/providers/kakao_auth_providers.dart';

class LoginPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final screenHeight = MediaQuery.of(context).size.height;

    return Scaffold(
      backgroundColor: Colors.white,
      body: SingleChildScrollView(
        child: Container(
          height: screenHeight, // 화면 전체 높이만큼 확보
          alignment: Alignment.center,
          padding: const EdgeInsets.symmetric(horizontal: 16),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              // 로고
              Image.asset(
                'assets/images/hungle_app_logo.png',
                width: 180,
              ),

              const SizedBox(height: 50),

              // 카카오 로그인 버튼
              Consumer<KakaoAuthProvider>(
                builder: (context, kakaoProvider, child) {
                  return GestureDetector(
                    onTap: kakaoProvider.isLoading
                        ? null
                        : () async {
                      await kakaoProvider.login();
                      if (kakaoProvider.isLoggedIn) {
                        Navigator.pushReplacement(
                          context,
                          HomeModule.getHomeRoute(loginType: "Kakao"),
                        );
                      }
                    },
                    child: Image.asset(
                      'assets/images/kakao_login.png',
                      width: 200,
                      height: 50,
                      fit: BoxFit.fill,
                    ),
                  );
                },
              ),

              const SizedBox(height: 10),
            ],
          ),
        ),
      ),
    );
  }
}
