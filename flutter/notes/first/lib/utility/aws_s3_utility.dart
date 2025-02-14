import 'dart:convert';
import 'dart:typed_data';
import 'package:http/http.dart' as http;
import 'package:crypto/crypto.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';

class AwsS3Utility {
  static final String bucketName = dotenv.env['AWS_BUCKET_NAME'] ?? '';
  static final String region = dotenv.env['AWS_REGION'] ?? '';
  static final String accessKey = dotenv.env['AWS_ACCESS_KEY_ID'] ?? '';
  static final String secretKey = dotenv.env['AWS_SECRET_ACCESS_KEY'] ?? '';

  // 파일 업로드 메서드 (Content-Type 헤더 없이 전송)
  static Future<String?> uploadFile(Uint8List fileBytes, String filePath) async {
    print("[INFO] Starting file upload...");
    final signedUrl = await _generateSignedUrl('PUT', filePath);
    print("[DEBUG] Generated Signed URL: $signedUrl");

    final response = await http.put(
      signedUrl,
      body: fileBytes,
      // Content-Type 헤더를 전송하지 않음.
    );

    print("[DEBUG] Response status: ${response.statusCode}");
    if (response.statusCode == 200) {
      print("[INFO] File uploaded successfully: $filePath");
      return "https://$bucketName.s3.$region.amazonaws.com/$filePath";
    } else {
      print("[ERROR] Upload failed: ${response.statusCode}");
      print("[ERROR] Response body: ${response.body}");
      return null;
    }
  }

  // URL 서명 생성 (Content-Type 헤더 없이 canonical request 생성)
  static Future<Uri> _generateSignedUrl(String method, String filePath) async {
    final service = 's3';
    final host = '$bucketName.s3.$region.amazonaws.com';
    final canonicalUri = '/$filePath';
    final algorithm = 'AWS4-HMAC-SHA256';
    final date = _getDate();
    final amzDate = _getAmzDate();
    final credentialScope = '$date/$region/$service/aws4_request';

    // Content-Type 헤더 없이 canonical headers 구성
    final canonicalHeaders =
        'host:$host\n'
        'x-amz-content-sha256:UNSIGNED-PAYLOAD\n'
        'x-amz-date:$amzDate\n';
    final signedHeaders = 'host;x-amz-content-sha256;x-amz-date';
    final canonicalRequest =
        "$method\n$canonicalUri\n\n$canonicalHeaders\n$signedHeaders\nUNSIGNED-PAYLOAD";

    final hashedCanonicalRequest =
    sha256.convert(utf8.encode(canonicalRequest)).toString();
    final stringToSign =
        "$algorithm\n$amzDate\n$credentialScope\n$hashedCanonicalRequest";

    final signingKey = _getSignatureKey(secretKey, date, region, service);
    final signature =
    Hmac(sha256, signingKey).convert(utf8.encode(stringToSign)).toString();

    return Uri.parse("https://$host$canonicalUri").replace(queryParameters: {
      'X-Amz-Algorithm': algorithm,
      'X-Amz-Credential': "$accessKey/$credentialScope",
      'X-Amz-Date': amzDate,
      'X-Amz-SignedHeaders': signedHeaders,
      'X-Amz-Signature': signature,
      'X-Amz-Expires': '3600', // 1시간
    });
  }

  // 날짜 관련 메서드들
  static String _getDate() {
    final now = DateTime.now().toUtc();
    return "${now.year}${_twoDigits(now.month)}${_twoDigits(now.day)}";
  }

  static String _getAmzDate() {
    final now = DateTime.now().toUtc();
    return "${now.year}${_twoDigits(now.month)}${_twoDigits(now.day)}T${_twoDigits(now.hour)}${_twoDigits(now.minute)}${_twoDigits(now.second)}Z";
  }

  static List<int> _getSignatureKey(String key, String date, String region, String service) {
    var kDate = Hmac(sha256, utf8.encode("AWS4$key")).convert(utf8.encode(date)).bytes;
    var kRegion = Hmac(sha256, kDate).convert(utf8.encode(region)).bytes;
    var kService = Hmac(sha256, kRegion).convert(utf8.encode(service)).bytes;
    var kSigning = Hmac(sha256, kService).convert(utf8.encode("aws4_request")).bytes;
    return kSigning;
  }

  static String _twoDigits(int n) {
    return n.toString().padLeft(2, '0');
  }
}
