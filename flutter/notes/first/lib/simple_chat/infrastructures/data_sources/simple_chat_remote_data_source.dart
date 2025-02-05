import 'dart:convert';
import 'package:http/http.dart' as http;

import 'package:flutter_dotenv/flutter_dotenv.dart';

class SimpleChatRemoteDataSource {

  Future<String> fetchLLMGeneratedText(String prompt) async {
    dotenv.load();
    String llmApiKey = dotenv.env['API_KEY'] ?? '';
    String llmApiUrl = dotenv.env['API_URL'] ?? '';

    final url = Uri.parse(llmApiUrl);
    final headers = { 'Authorization': 'Bearer $llmApiKey', 'Content-Type': 'application/json' };
    final body = { 'inputs': prompt };

    final response = await http.post(
      url,
      headers: headers,
      body: json.encode(body)
    );
    
    if (response.statusCode == 200) {
      final data = json.decode(response.body);
      if (data.isNotEmpty && data[0]['generated_text'] != null) {
        return data[0]['generated_text'];
      } else {
        throw Exception("텍스트 생성 실패");
      }
    } else {
      throw Exception("응답 확보 실패");
    }
  }
}