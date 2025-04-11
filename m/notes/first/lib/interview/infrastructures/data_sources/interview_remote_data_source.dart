import 'dart:convert';
import 'package:first/interview/domain/entity/interview.dart';
import 'package:first/interview/domain/usecases/list/response/interview_list_response.dart';
import 'package:http/http.dart' as http;

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
        title: data['title'] ?? 'No Title',  // title 추가
        companyName: data['companyName'] ?? 'Unknown',
        jobTitle: data['jobTitle'] ?? 'Unknown',
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

  int parseInt(dynamic value) {
    if (value is String) {
      return int.tryParse(value) ?? 0;
    }

    return value ?? 0;
  }
}
