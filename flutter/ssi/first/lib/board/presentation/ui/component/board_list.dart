import 'package:flutter/cupertino.dart';

import 'card_item.dart';

class BoardList extends StatelessWidget {
  final List<dynamic> boardList;

  BoardList({
    required this.boardList
  });

  @override
  Widget build(BuildContext context) {
    return Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: List.generate(boardList.length, (index) {
          final board = boardList[index];
          if (board == null) {
            return SizedBox(height: 20);
          }

          return CardItem(
              title: board.title,
              content: board.content,
              nickname: board.nickname,
              createDate: board.createDate,
              onTap: () async {
                print("읽기 연산 구현");
              }
          );
        })
    );
  }
}