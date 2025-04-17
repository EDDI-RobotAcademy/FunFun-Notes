import '../create/response/interview_followup_response.dart';

abstract class CreateInterviewQuestionAnswerUseCase {
  Future<InterviewFollowupResponse?> create({
    required String userToken,
    required int interviewId,
    required int questionId,
    required String answerText,
  });
}