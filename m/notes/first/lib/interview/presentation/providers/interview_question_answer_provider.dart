import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class InterviewQuestionAnswerProvider extends ChangeNotifier {
  // final InterviewQuestionAnswerUseCase interviewQuestionAnswerUseCase;
  final FlutterSecureStorage _secureStorage = const FlutterSecureStorage();

  // InterviewQuestionAnswerProvider({required this.interviewQuestionAnswerUseCase});

  bool _isLoading = false;
  bool get isLoading => _isLoading;

  String? _errorMessage;
  String? get errorMessage => _errorMessage;

  Future<void> create(String answerText) async {
    print("전송할 답변: $answerText");
    
    _isLoading = true;
    notifyListeners();

    try {
      final userToken = await _secureStorage.read(key: 'userToken');

      if (userToken == null) {
        throw Exception('로그인 정보가 없습니다. 다시 로그인해주세요.');
      }

      // await interviewQuestionAnswerUseCase.create(userToken, answerText);
      _errorMessage = null;
    } catch (e) {
      _errorMessage = '답변 전송 실패: $e';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
