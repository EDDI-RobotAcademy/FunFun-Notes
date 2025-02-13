import 'dart:io';

import 'package:flutter/cupertino.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';
import 'package:vsc_quill_delta_to_html/vsc_quill_delta_to_html.dart';

import 'package:flutter_aws_s3_client/flutter_aws_s3_client.dart';
import 'package:path_provider/path_provider.dart';

import '../../domain/entity/blog_post.dart';

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
}