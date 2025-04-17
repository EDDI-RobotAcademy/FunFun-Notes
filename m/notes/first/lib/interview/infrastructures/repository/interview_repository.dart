import '../../domain/entity/interview.dart';
import '../../domain/usecases/create/response/interview_create_response.dart';
import '../../domain/usecases/create/response/interview_followup_response.dart';
import '../../domain/usecases/list/response/interview_list_response.dart';

abstract class InterviewRepository {
  Future<InterviewListResponse> listInterview(int page, int perPage, String userToken);
  Future<InterviewCreateResponse> createInterview(String userToken, Interview interview);
  Future<InterviewFollowupResponse?> createInterviewQuestionAnswer({
    required String userToken,
    required int interviewId,
    required int questionId,
    required String answerText,
  });
}
