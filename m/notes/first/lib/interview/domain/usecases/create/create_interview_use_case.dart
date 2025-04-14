import 'package:first/interview/domain/usecases/create/response/interview_create_response.dart';

import '../../entity/interview.dart';

abstract class CreateInterviewUseCase {
  Future<InterviewCreateResponse> createInterview(String userToken, Interview interview);
}
