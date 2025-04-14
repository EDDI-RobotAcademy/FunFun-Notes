import 'package:flutter/material.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import '../../domain/entity/interview.dart';
import '../../domain/usecases/create/create_interview_use_case.dart';

class InterviewCreateProvider extends ChangeNotifier {
  final CreateInterviewUseCase createInterviewUseCase;
  final FlutterSecureStorage _secureStorage = const FlutterSecureStorage();

  InterviewCreateProvider({required this.createInterviewUseCase});

  bool _isLoading = false;
  bool get isLoading => _isLoading;

  String? _errorMessage;
  String? get errorMessage => _errorMessage;

  Future<void> createInterview(Interview interview) async {
    _isLoading = true;
    notifyListeners();

    try {
      final userToken = await _secureStorage.read(key: 'userToken');

      if (userToken == null) {
        throw Exception('로그인 정보가 없습니다. 다시 로그인해주세요.');
      }

      await createInterviewUseCase.createInterview(userToken, interview);
      _errorMessage = null; // 성공시 에러 메시지 초기화
    } catch (e) {
      _errorMessage = '면접 설정 실패: $e';
    } finally {
      _isLoading = false;
      notifyListeners();
    }
  }
}
