import 'dart:convert';
import 'dart:io';
import 'package:http/http.dart' as http;
import 'package:crypto/crypto.dart';
import 'package:uuid/uuid.dart';
import 'package:path/path.dart' as path;
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class AwsS3Utility {
  static const String bucketName = "your-bucket-name";
  static const String region = "your-region";
  static const String accessKey = "your-access-key";
  static const String secretKey = "your-secret-key";
  static const String endpoint = "https://s3.$region.amazonaws.com"; // S3 endpoint URL

  // AWS S3에 파일 업로드 함수
  static Future<String?> uploadHtmlContent(String htmlContent) async {
    try {
      final uuid = Uuid().v4();
      final fileName = "$uuid.html"; // Unique file name using UUID
      final filePath = "/blog-post/$fileName";

      // 1. 업로드할 파일을 임시로 로컬 파일로 저장
      final tempDir = await Directory.systemTemp.createTemp();
      final file = File(path.join(tempDir.path, fileName));
      await file.writeAsString(htmlContent);

      // 2. 서명된 URL 생성
      final url = Uri.parse("$endpoint/$bucketName$filePath");
      final signedUrl = await _generateSignedUrl(url, file);

      // 3. HTTP 요청을 통해 S3에 파일 업로드
      final request = http.MultipartRequest('PUT', signedUrl);
      request.files.add(await http.MultipartFile.fromPath('file', file.path));

      final response = await request.send();

      if (response.statusCode == 200) {
        // 업로드 성공
        print("파일 업로드 성공: $filePath");
        return "https://$bucketName.s3.$region.amazonaws.com$filePath";
      } else {
        print("업로드 실패: ${response.statusCode}");
        return null;
      }
    } catch (e) {
      print("S3 업로드 실패: $e");
      return null;
    }
  }

  // AWS S3에 대한 서명된 URL을 생성하는 함수
  static Future<Uri> _generateSignedUrl(Uri url, File file) async {
    // 여기서 AWS Signature V4를 사용하여 서명된 URL을 생성합니다.
    // 실제로 서명된 URL을 생성하는 방법은 AWS 문서에서 확인 가능합니다.
    // 자세한 구현은 복잡하므로, 서명된 URL을 생성하는 라이브러리나 서비스를 사용하는 것이 좋습니다.

    final headers = <String, String>{
      'x-amz-date': _getAmzDate(),
      'Authorization': 'AWS4-HMAC-SHA256 Credential=$accessKey/${_getDate()}/$region/s3/aws4_request, SignedHeaders=host;x-amz-date, Signature=<signature>',
    };

    return url.replace(queryParameters: headers); // 서명된 URL 반환
  }

  // AWS S3 서명에 필요한 날짜 형식
  static String _getDate() {
    final now = DateTime.now().toUtc();
    return "${now.year}${_pad(now.month)}${_pad(now.day)}";
  }

  // AWS S3 서명에 필요한 날짜 형식 (예: 20230201)
  static String _getAmzDate() {
    final now = DateTime.now().toUtc();
    return "${_getDate()}T${_pad(now.hour)}${_pad(now.minute)}${_pad(now.second)}Z";
  }

  static String _pad(int value) {
    return value.toString().padLeft(2, '0');
  }
}
