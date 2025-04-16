import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../../domain/entity/interview.dart';
import '../../domain/usecases/create/create_interview_use_case.dart';
import '../../domain/usecases/create/response/interview_create_response.dart';

class InterviewCreateProvider extends ChangeNotifier {
  final CreateInterviewUseCase createInterviewUseCase;
  final FlutterSecureStorage _secureStorage = const FlutterSecureStorage();

  InterviewCreateProvider({required this.createInterviewUseCase});

  bool _isLoading = false;
  bool get isLoading => _isLoading;

  String? _errorMessage;
  String? get errorMessage => _errorMessage;

  int? _createdInterviewId;
  int? get createdInterviewId => _createdInterviewId;

  Future<InterviewCreateResponse?> createInterview(Interview interview) async {
    _isLoading = true;
    notifyListeners();

    try {
      final userToken = await _secureStorage.read(key: 'userToken');

      if (userToken == null) {
        throw Exception('로그인 정보가 없습니다. 다시 로그인해주세요.');
      }

      final response = await createInterviewUseCase.createInterview(userToken, interview);

      print('[🔍 DEBUG] 받은 응답:');
      print('Interview ID: ${response.interviewId}');
      print('Question ID: ${response.questionId}');
      print('Question: "${response.question}"');

      _createdInterviewId = response.interviewId;

      _errorMessage = null;
      return response;
    } catch (e) {
      _errorMessage = '면접 설정 실패: $e';
      _createdInterviewId = null;
      return null;
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}

