import 'package:first/board/presentation/providers/board_list_provider.dart';
import 'package:first/board/presentation/ui/board_list_page.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';
import 'package:provider/single_child_widget.dart';

import 'domain/usecases/list/ListBoardUseCaseImpl.dart';
import 'infrasturctures/data_sources/board_remote_data_source.dart';
import 'infrasturctures/repository/board_repository_impl.dart';

class BoardModule {
  static final String baseUrl = dotenv.env['BASE_URL'] ?? '';

  static final boardRemoteDataSource = BoardRemoteDataSource(baseUrl);
  static final boardRepository = BoardRepositoryImpl(boardRemoteDataSource);

  static final listBoardUseCase = ListBoardUseCaseImpl(boardRepository);

  static List<SingleChildWidget> provideCommonProviders () {
    return [
      Provider(create: (_) => listBoardUseCase),
    ];
  }

  static Widget provideBoardListPage() {
    return MultiProvider(
      providers: [
        ...provideCommonProviders(),
        ChangeNotifierProvider(
          create: (_) =>
            BoardListProvider(listBoardUseCase: listBoardUseCase),
        )
      ],
      child: BoardListPage(),
    );
  }
}