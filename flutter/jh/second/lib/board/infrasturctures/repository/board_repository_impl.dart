import 'package:second/board/domain/entity/board.dart';
import 'package:second/board/domain/usecases/list/response/board_list_response.dart';

import '../data_sources/board_remote_data_source.dart';
import 'board_repository.dart';

class BoardRepositoryImpl implements BoardRepository {
  final BoardRemoteDataSource boardRemoteDataSource;

  BoardRepositoryImpl(this.boardRemoteDataSource);

  @override
  Future<BoardListResponse> listBoard(int page, int perPage) async {
    final boardListResponse =
      await boardRemoteDataSource.listBoard(page, perPage);

    return boardListResponse;
  }

  @override
  Future<Board> create(String title, String content, String userToken) async {
    try {
      final board = await boardRemoteDataSource.create(title, content, userToken);
      return board;
    } catch (e) {
      print("오류 발생: $e");
      throw Exception('게시물 생성 실패');
    }
  }
}