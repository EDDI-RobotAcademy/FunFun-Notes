import 'package:first/common_ui/custom_app_bar.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/board_list_provider.dart';

class BoardListPage extends StatefulWidget {
  @override
  _BoardListPageState createState() => _BoardListPageState();
}

class _BoardListPageState extends State<BoardListPage> {
  late ScrollController scrollController;
  
  @override
  void initState() {
    super.initState();
    scrollController = ScrollController();
    
    // 실제 데이터가 전부 준비 된 이후 화면 출력하도록 만듬
    WidgetsBinding.instance.addPostFrameCallback((_) {
      final boardListProvider =
        Provider.of<BoardListProvider>(context, listen: false);

      boardListProvider.listBoard(1, 6);
    });
  }
  
  @override
  void dispose() {
    scrollController.dispose();
    super.dispose();
  }

  void onPageChanged(int page) {
    final boardListProvider =
      Provider.of<BoardListProvider>(context, listen: false);

    boardListProvider.listBoard(page, 6);
  }

  @override
  Widget build(BuildContext context) {
    
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: Size.fromHeight(kToolbarHeight),
        child: CustomAppBar(
          body: Container(),
          title: '게시판',
        ),
      ),
    );
  }

}