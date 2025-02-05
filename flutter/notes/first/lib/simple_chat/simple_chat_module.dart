import 'package:first/kakao_authentication/presentation/providers/kakao_auth_providers.dart';
import 'package:first/kakao_authentication/presentation/ui/kakao_login_page.dart';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class SimpleChatModule {
  static Widget provideSimpleChatPage() {
    return MultiProvider(
      providers: [
        Provider<SimpleChatRemoteDataSource>(
          create: (_) => SimpleChatRemoteDataSource()
        ),
        ProxyProvider<SimpleChatRemoteDataSource, SimpleChatRepository>(
          update: (_, remoteDataSource, __) =>
            SimpleChatRepositoryImpl(remoteDataSource),
        ),
        ProxyProvider<SimpleChatRepository, SendSimpleChatUseCaseImpl>(
          update: (_, repository, __) =>
            SendSimpleChatUseCaseImpl(repository)
        ),
        ChangeNotifierProvider<SendSimpleChatUseCaseImpl, SimpleChatProvider>(
          create: (context) => SimpleChatProvider(
            sendSimpleChatUseCase: context.read<SendSimpleChatUseCaseImpl>(),
          ),
          update: (_, useCase, previousProvider) {
            previousProvider?.updateUseCase(useCase);
            return previousProvider ?? SimpleChatProvider(sendSimpleChatUseCase: useCase);
          }
        ),
      ],
      child: SimpleChatPage()
    );
  }
}