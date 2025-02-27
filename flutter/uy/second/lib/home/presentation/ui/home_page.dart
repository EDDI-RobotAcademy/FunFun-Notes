import 'package:provider/provider.dart';
import 'package:second/common_ui/custom_app_bar.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../../../kakao_authentication/presentation/providers/kakao_auth_providers.dart';

class HomePage extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    final kakaoAuthProvider = Provider.of<KakaoAuthProvider>(context);

    return Scaffold(
      body: CustomAppBar(
        body: Center(
            child: Text(
              kakaoAuthProvider.isLoggedIn
                  ? 'Welcome to HomePage'
                  : "Use after login",
              textAlign: TextAlign.center,
              style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold),
            )
        ),
      ),
    );
  }
}