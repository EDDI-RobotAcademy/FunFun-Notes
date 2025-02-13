import 'dart:io';

import 'package:flutter/cupertino.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:vsc_quill_delta_to_html/vsc_quill_delta_to_html.dart';

import '../../../utility/aws_s3_utility.dart';
import '../../domain/entity/blog_post.dart';
import '../../domain/usecases/create/create_blog_post_use_case.dart';

class BlogPostCreateProvider with ChangeNotifier {
  final CreateBlogPostUseCase createBlogPostUseCase;
  final FlutterSecureStorage secureStorage = FlutterSecureStorage();

  BlogPostCreateProvider({
    required this.createBlogPostUseCase
  });

  bool isLoading = false;
  String message = '';

  Future<BlogPost?> createBlogPost(String title, String content) async {
    isLoading = true;
    notifyListeners();

    try {
      final userToken = await secureStorage.read(key: 'userToken');

      if (userToken == null) {
        message = '로그인 상태가 아니므로 로그인을 먼저 해주세요.';
        isLoading = false;
        notifyListeners();
        return null;
      }

      final blogPost = await createBlogPostUseCase.execute(title, content, userToken);

      return blogPost;
    } catch (e) {
      message = '게시물 생성에 실패했습니다. 오류: $e';
      return null;
    } finally {
      isLoading = false;
      notifyListeners();
    }
  }

  /// Delta JSON -> HTML 변환
  String convertDeltaToHtml(List<dynamic> deltaJson) {
    final converter = QuillDeltaToHtmlConverter(List.castFrom(deltaJson));
    return converter.convert();
  }

  /// HTML을 S3에 업로드
  Future<String?> uploadToS3(String htmlContent) async {
    return await AwsS3Utility.uploadHtmlContent(htmlContent);
  }
}