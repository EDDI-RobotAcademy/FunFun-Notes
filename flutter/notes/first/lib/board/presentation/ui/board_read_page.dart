import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../providers/board_read_provider.dart';

class BoardReadPage extends StatefulWidget {
  @override
  _BoardReadPageState createState() => _BoardReadPageState();
}

class _BoardReadPageState extends State<BoardReadPage> {

  @override
  void initState() {
    super.initState();

    final boardReadProvider = Provider.of<BoardReadProvider>(context, listen: false);

    if (boardReadProvider.board == null) {
      boardReadProvider.fetchBoard();
    }
  }

  Future<bool> _onWillPop() async {
    final boardReadProvider = Provider.of<BoardReadProvider>(context, listen: false);

    return Future.value(false);
  }

  @override
  Widget build(BuildContext context) {
    final boardReadProvider = Provider.of<BoardReadProvider>(context, listen: false);

    return WillPopScope(
      onWillPop: _onWillPop,
      child: Scaffold(
        appBar: AppBar(
          title: Text('게시물 읽기'),
          actions: [
            IconButton(
              onPressed: () {
                final selectedBoard = boardReadProvider.board;
                print("수정 클릭");
              },
              icon: Icon(Icons.edit)
            ),
            IconButton(
              onPressed: () { print("삭제 클릭"); },
              icon: Icon(Icons.delete)
            )
          ],
        ),
      ),
    );
  }
}