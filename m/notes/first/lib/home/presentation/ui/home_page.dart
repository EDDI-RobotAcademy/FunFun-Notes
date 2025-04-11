import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../../authentication/presentation/ui/login_page.dart';
import '../../../kakao_authentication/presentation/providers/kakao_auth_providers.dart';
import '../../../common_ui/custom_app_bar.dart'; // CustomAppBar import 추가

class HomePage extends StatefulWidget {
  final String loginType;

  const HomePage({Key? key, required this.loginType}) : super(key: key);

  @override
  _HomePageState createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  String userEmail = "이메일을 불러오는 중...";
  String userNickname = "아무개";

  @override
  void initState() {
    super.initState();
    _fetchUserInfo();
  }

  Future<void> _fetchUserInfo() async {
    try {
      if (widget.loginType == "Kakao") {
        final kakaoProvider = Provider.of<KakaoAuthProvider>(context, listen: false);
        // final userInfo = await kakaoProvider.fetchUserInfo();
        // setState(() {
        //   userEmail = userInfo.kakaoAccount?.email ?? "이메일 정보 없음";
        //   userNickname = userInfo.kakaoAccount?.profile?.nickname ?? "닉네임 없음";
        // });
      } else if (widget.loginType == "Naver") {
        // final naverProvider = Provider.of<NaverAuthProvider>(context, listen: false);
        // final userInfo = await naverProvider.fetchUserInfo();
        // setState(() {
        //   userEmail = userInfo.email ?? "이메일 정보 없음";
        //   userNickname = userInfo.nickname ?? "닉네임 없음";
        // });
      }
    } catch (error) {
      setState(() {
        userEmail = "이메일 불러오기 실패";
        userNickname = "닉네임 불러오기 실패";
      });
    }
  }

  void _logout() async {
    if (widget.loginType == "Kakao") {
      // final kakaoRemote = Provider.of<KakaoAuthRemoteDataSource>(context, listen: false);
      // await kakaoRemote.logoutFromKakao();
      // Provider.of<KakaoAuthProvider>(context, listen: false).logout();
    } else if (widget.loginType == "Naver") {
      // final naverRemote = Provider.of<NaverAuthRemoteDataSource>(context, listen: false);
      // await naverRemote.logoutFromNaver();
      // Provider.of<NaverAuthProvider>(context, listen: false).logout();
    }

    Navigator.pushReplacement(
      context,
      MaterialPageRoute(builder: (context) => LoginPage()),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: Size.fromHeight(kToolbarHeight),
        child: CustomAppBar(
          body: Container(),
          title: '홈페이지',
        ),
      ),
      backgroundColor: Colors.white,
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          crossAxisAlignment: CrossAxisAlignment.center,
          children: [
            Text(
              "안녕하세요, $userNickname 님!",
              style: TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 8),
            Text(
              "이메일: $userEmail",
              style: TextStyle(fontSize: 16),
            ),
            SizedBox(height: 12),
            Text(
              "EDDI Test App",
              style: TextStyle(fontSize: 18),
            ),
          ],
        ),
      ),
    );
  }
}
