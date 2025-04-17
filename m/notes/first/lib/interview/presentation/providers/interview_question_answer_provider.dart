import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import '../../domain/usecases/create/response/interview_followup_response.dart';
import '../../domain/usecases/create_answer/create_interview_question_answer_use_case.dart';

class InterviewQuestionAnswerProvider extends ChangeNotifier {
  final CreateInterviewQuestionAnswerUseCase createInterviewQuestionAnswerUseCase;
  final FlutterSecureStorage _secureStorage = const FlutterSecureStorage();

  InterviewQuestionAnswerProvider({required this.createInterviewQuestionAnswerUseCase});

  bool _isLoading = false;
  bool get isLoading => _isLoading;

  String? _errorMessage;
  String? get errorMessage => _errorMessage;

  Future<InterviewFollowupResponse?> create({
    required String answerText,
    required int interviewId,
    required int questionId,
  }) async {
    _setLoading(true);

    try {
      final userToken = await _secureStorage.read(key: 'userToken');

      if (userToken == null || userToken.isEmpty) {
        throw Exception('로그인 정보가 없습니다. 다시 로그인해주세요.');
      }

      final followupResponse = await createInterviewQuestionAnswerUseCase.create(
        userToken: userToken,
        answerText: answerText,
        interviewId: interviewId,
        questionId: questionId,
      );

      if (followupResponse == null) {
        _errorMessage = '답변 전송에 실패했습니다. 다시 시도해주세요.';
      } else {
        _errorMessage = null;
      }

      return followupResponse;
    } catch (e) {
      _errorMessage = '답변 전송 실패: ${e.toString()}';
    } finally {
      _setLoading(false);
    }
  }

  void _setLoading(bool value) {
    _isLoading = value;
    notifyListeners();
  }
}
