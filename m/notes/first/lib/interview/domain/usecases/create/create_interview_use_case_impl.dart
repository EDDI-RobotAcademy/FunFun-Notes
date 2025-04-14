import 'package:first/interview/domain/usecases/create/response/interview_create_response.dart';
import 'package:first/interview/infrastructures/repository/interview_repository_impl.dart';

import '../../entity/interview.dart';
import 'create_interview_use_case.dart';

class CreateInterviewUseCaseImpl implements CreateInterviewUseCase {
  final InterviewRepositoryImpl interviewRepository;

  CreateInterviewUseCaseImpl(this.interviewRepository);

  @override
  Future<InterviewCreateResponse> createInterview(String userToken, Interview interview) async {
    try {
      final response = await interviewRepository.createInterview(userToken, interview);
      return response;
    } catch (e) {
      throw Exception('Failed to create interview: $e');
    }
  }
}
