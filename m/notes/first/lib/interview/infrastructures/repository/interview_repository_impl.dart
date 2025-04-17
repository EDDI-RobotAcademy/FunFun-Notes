import '../../domain/entity/interview.dart';
import '../../domain/usecases/create/response/interview_create_response.dart';
import '../../domain/usecases/create/response/interview_followup_response.dart';
import '../../domain/usecases/list/response/interview_list_response.dart';
import '../data_sources/interview_remote_data_source.dart';
import 'interview_repository.dart';

class InterviewRepositoryImpl implements InterviewRepository {
  final InterviewRemoteDataSource remoteDataSource;

  InterviewRepositoryImpl(this.remoteDataSource);

  @override
  Future<InterviewListResponse> listInterview(int page, int perPage, String userToken) async {
    final interviewListResponse = await remoteDataSource.listInterview(page, perPage, userToken);

    return interviewListResponse;
  }

  @override
  Future<InterviewCreateResponse> createInterview(String userToken, Interview interview) {
    return remoteDataSource.createInterview(userToken, interview);
  }

  @override
  Future<InterviewFollowupResponse?> createInterviewQuestionAnswer({required String userToken, required int interviewId, required int questionId, required String answerText}) {
    return remoteDataSource.createInterviewQuestionAnswer(
      userToken: userToken,
      interviewId: interviewId,
      questionId: questionId,
      answerText: answerText,
    );
  }
}
