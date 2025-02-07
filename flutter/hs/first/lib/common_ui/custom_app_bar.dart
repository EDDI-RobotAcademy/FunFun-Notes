import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

import '../kakao_authentication/kakao_auth_module.dart';
import 'app_bar_action.dart';

class CustomAppBar extends StatelessWidget {
  final Widget body;
  final String title;

  CustomAppBar({
    required this.body,
    this.title = 'Home'
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      children: [
        AppBar(
          title: Text(title),
          backgroundColor: Colors.deepPurple,
          actions: [
            AppBarAction(
              icon: Icons.login,
              tooltip: 'Login',
              onPressed: () {
                Navigator.push(
                  context,
                  MaterialPageRoute(
                    builder: (context) => KakaoAuthModule.provideKakaoLoginPage()
                  ),
                );
              },
            )
          ],
        ),
        Expanded(child: body)
      ],
    );
  }
}