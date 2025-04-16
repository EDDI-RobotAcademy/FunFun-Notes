import 'package:first/interview/presentation/providers/interview_create_provider.dart';
import 'package:first/interview/presentation/providers/interview_question_answer_provider.dart';
import 'package:first/interview/presentation/ui/interview_ready_page.dart';
import 'package:first/interview/presentation/ui/interview_start_page.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:provider/provider.dart';
import 'package:provider/single_child_widget.dart';

import 'domain/usecases/create/create_interview_use_case_impl.dart';
import 'domain/usecases/list/list_interview_use_case_impl.dart';
import 'infrastructures/data_sources/interview_remote_data_source.dart';
import 'infrastructures/repository/interview_repository_impl.dart';
import 'presentation/providers/interview_list_provider.dart';
import 'presentation/ui/interview_list_page.dart';

class InterviewModule {
  static final String baseUrl = dotenv.env['BASE_URL'] ?? '';

  static final interviewRemoteDataSource = InterviewRemoteDataSource(baseUrl);
  static final interviewRepository = InterviewRepositoryImpl(interviewRemoteDataSource);

  static final listInterviewUseCase = ListInterviewUseCaseImpl(interviewRepository);
  static final createInterviewUseCase = CreateInterviewUseCaseImpl(interviewRepository);
  // static final interviewDetailUseCase = InterviewDetailUseCaseImpl(interviewRepository);

  static List<SingleChildWidget> provideCommonProviders() {
    return [
      Provider(create: (_) => listInterviewUseCase),
      Provider(create: (_) => createInterviewUseCase),
      // Provider(create: (_) => interviewDetailUseCase),
    ];
  }

  static Widget provideInterviewListPage() {
    return MultiProvider(
      providers: [
        ...provideCommonProviders(),
        ChangeNotifierProvider(
          create: (_) =>
              InterviewListProvider(listInterviewUseCase: listInterviewUseCase)
        ),
      ],
      child: InterviewListPage(),
    );
  }

  static Widget provideInterviewReadyPage() {
    return MultiProvider(
      providers: [
        ...provideCommonProviders(),
        ChangeNotifierProvider(
          create: (_) => InterviewCreateProvider(createInterviewUseCase: createInterviewUseCase),
        ),
      ],
      child: InterviewReadyPage(),
    );
  }

  static Widget provideInterviewStartPage({
    required int interviewId,
    required int questionId,
    required String question,
  }) {
    return MultiProvider(
      providers: [
        ...provideCommonProviders(),
        ChangeNotifierProvider(
          create: (_) => InterviewQuestionAnswerProvider(),
        ),
      ],
      child: InterviewStartPage(
        interviewId: interviewId,
        questionId: questionId,
        question: question,
      ),
    );
  }
}
