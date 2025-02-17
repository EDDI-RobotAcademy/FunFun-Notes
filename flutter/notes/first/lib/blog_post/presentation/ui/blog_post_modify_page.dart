import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_secure_storage/flutter_secure_storage.dart';

import 'component/blog_post_modify_provider.dart';


class BlogPostModifyPage extends StatefulWidget {
  final int blogPostId;
  final String initialTitle;
  final String initialContent;

  BlogPostModifyPage({
    required this.blogPostId,
    required this.initialTitle,
    required this.initialContent,
  });

  @override
  _BlogPostModifyPageState createState() => _BlogPostModifyPageState();
}

class _BlogPostModifyPageState extends State<BlogPostModifyPage> {
  late TextEditingController _titleController;
  late TextEditingController _contentController;
  final FlutterSecureStorage _secureStorage = FlutterSecureStorage();

  @override
  void initState() {
    super.initState();

    _titleController = TextEditingController(text: widget.initialTitle);
    _contentController = TextEditingController(text: widget.initialContent);
  }

  @override
  Widget build(BuildContext context) {
    final blogPostModifyProvider = Provider.of<BlogPostModifyProvider>(context);

    if (blogPostModifyProvider.isLoading) {
      return Center(child: CircularProgressIndicator());
    }

    return Scaffold(
      appBar: AppBar(
        title: Text('블로그 포스트 수정'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            TextFormField(
              controller: _titleController,
              decoration: InputDecoration(labelText: '제목'),
            ),
            TextFormField(
              controller: _contentController,
              decoration: InputDecoration(labelText: '내용'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: _submitUpdate,
              child: Text('수정 완료'),
            ),
          ],
        ),
      ),
    );
  }

  void _submitUpdate() {
    final updatedTitle = _titleController.text;
    final updatedContent = _contentController.text;

    print("Updated Title: $updatedTitle");
    print("Updated Content: $updatedContent");

    _getUserTokenAndUpdate(updatedTitle, updatedContent);
  }

  Future<void> _getUserTokenAndUpdate(String title, String content) async {
    try {
      final userToken = await _secureStorage.read(key: 'userToken');
      print("Fetched userToken: $userToken");

      if (userToken == null) {
        throw Exception('User is not logged in.');
      }

      final blogPostModifyProvider =
          Provider.of<BlogPostModifyProvider>(context, listen: false);
      await blogPostModifyProvider.updateBlogPost(title, content, userToken);

      print("BlogPost updated successfully");
      Navigator.of(context).pop({'title': title, 'content': content});
    } catch (e) {
      print("Error during blogPost update: $e");
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('블로그 포스트 수정 실패: ${e.toString()}')),
      );
    }
  }

  @override
  void dispose() {
    _titleController.dispose();
    _contentController.dispose();
    super.dispose();
  }
}
