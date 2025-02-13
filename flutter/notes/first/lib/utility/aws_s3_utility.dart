import 'dart:io';
import 'package:amazon_s3_cognito/amazon_s3_cognito.dart';
import 'package:path_provider/path_provider.dart';
import 'package:uuid/uuid.dart';

class AwsS3Utility {
  static const String bucketName = "your-s3-bucket";
  static const String identityPoolId = "your-identity-pool-id";
  static const String region = "your-region"; // e.g., "us-east-1"

  /// 🔹 HTML 파일을 로컬에 저장 후 S3 업로드
  static Future<String?> uploadHtmlContent(String htmlContent) async {
    try {
      final dir = await getTemporaryDirectory();
      final filePath = "${dir.path}/${Uuid().v4()}.html";

      // HTML 내용을 파일로 저장
      final file = File(filePath);
      await file.writeAsString(htmlContent, flush: true);

      // 🚀 S3 업로드
      final uploadedUrl = await AmazonS3Cognito.upload(
        filePath,           // ⬅️ 경로만 넘긴다
        bucketName,
        identityPoolId,
        region,
        path.basename(filePath),
      );

      return uploadedUrl;  // 업로드된 S3 URL 반환
    } catch (e) {
      print("❌ S3 업로드 실패: $e");
      return null;
    }
  }
}
