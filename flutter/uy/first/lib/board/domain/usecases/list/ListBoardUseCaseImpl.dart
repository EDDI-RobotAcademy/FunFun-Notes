import 'package:first/board/domain/usecases/list/response/board_list_response.dart';

import '../../../infrastructures/repository/board_repository.dart';
import 'ListBoardUseCase.dart';

class ListBoardUseCaseImpl implements ListBoardUseCase {
  final BoardRepository boardRepository;

  ListBoardUseCaseImpl(this.boardRepository);

  @override
  Future<BoardListResponse> call(int page, int perPage) async {
    try {
      final BoardListResponse response =
      await boardRepository.listBoard(page, perPage);

      return response;
    } catch (e) {
      throw Exception('Failed to fetch board');
    }
  }
}