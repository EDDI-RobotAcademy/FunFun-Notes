import 'package:first/board/domain/usecases/list/response/board_list_response.dart';

abstract class BoardRepository {
  Future<BoardListResponse> listBoard(int page, int perPage);
}