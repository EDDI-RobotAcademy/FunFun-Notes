import '../../../infrastructures/repository/interview_repository.dart';
import '../create/response/interview_followup_response.dart';
import 'create_interview_question_answer_use_case.dart';

class CreateInterviewQuestionAnswerUseCaseImpl implements CreateInterviewQuestionAnswerUseCase {
  final InterviewRepository repository;

  CreateInterviewQuestionAnswerUseCaseImpl(this.repository);

  @override
  Future<InterviewFollowupResponse?> create({
    required String userToken,
    required int interviewId,
    required int questionId,
    required String answerText,
  }) {
    return repository.createInterviewQuestionAnswer(
      userToken: userToken,
      interviewId: interviewId,
      questionId: questionId,
      answerText: answerText,
    );
  }
}
