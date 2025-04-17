import 'dart:convert';
import 'package:first/interview/domain/entity/interview.dart';
import 'package:first/interview/domain/usecases/list/response/interview_list_response.dart';
import 'package:http/http.dart' as http;

import '../../domain/usecases/create/response/interview_create_response.dart';
import '../../domain/usecases/create/response/interview_followup_response.dart';

class InterviewRemoteDataSource {
  final String baseUrl;

  InterviewRemoteDataSource(this.baseUrl);

  Future<InterviewListResponse> listInterview(int page, int perPage, String userToken) async {
    final parsedUri = Uri.parse('$baseUrl/interview/list');

    // POST 요청에 필요한 body 데이터
    final requestBody = {
      'userToken': userToken,
      'page': page,
      'perPage': perPage,
    };

    final response = await http.post(
      parsedUri,
      headers: {'Content-Type': 'application/json'},
      body: json.encode(requestBody),  // body에 JSON 데이터 전송
    );

    if (response.statusCode == 200) {
      final data = json.decode(response.body);

      List<Interview> interviewList = (data['interviewList'] as List)
          .map((data) => Interview(
        id: data['id'] ?? 0,  // id 추가
        jobCategory: data['jobCategory'] ?? 'Unknown',
        createDate: data['createDate'] ?? 'Unknown',  // createDate 추가
      ))
          .toList();

      int totalItems = parseInt(data['totalItems']);
      int totalPages = parseInt(data['totalPages']);

      return InterviewListResponse(
        interviewList: interviewList,
        totalItems: totalItems,
        totalPages: totalPages,
      );
    } else {
      throw Exception('인터뷰 목록 조회 실패');
    }
  }

  Future<InterviewCreateResponse> createInterview(String userToken, Interview interview) async {
    final uri = Uri.parse('$baseUrl/interview/create');

    final response = await http.post(
      uri,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'userToken': userToken,
        'jobCategory': interview.jobCategory,
        'experienceLevel': interview.experienceLevel,
      }),
    );

    print('[📥 응답 바디]');
    print(response.body);

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body);
      return InterviewCreateResponse.fromJson(data); // ✅ interviewId만 있으면 되는 구조
    } else {
      throw Exception('인터뷰 세션 생성 실패');
    }
  }

  Future<InterviewFollowupResponse?> createInterviewQuestionAnswer({
    required String userToken,
    required int interviewId,
    required int questionId,
    required String answerText,
  }) async {
    final uri = Uri.parse('$baseUrl/interview/user-answer');

    final response = await http.post(
      uri,
      headers: {'Content-Type': 'application/json'},
      body: jsonEncode({
        'userToken': userToken,
        'interviewId': interviewId,
        'questionId': questionId,
        'answerText': answerText,
      }),
    );

    if (response.statusCode == 200) {
      final Map<String, dynamic> data = jsonDecode(response.body);
      return InterviewFollowupResponse.fromJson(data);
    } else {
      print('❌ 서버 에러: ${response.statusCode} - ${response.body}');
      return null;
    }
  }

  int parseInt(dynamic value) {
    if (value is String) {
      return int.tryParse(value) ?? 0;
    }

    return value ?? 0;
  }
}
