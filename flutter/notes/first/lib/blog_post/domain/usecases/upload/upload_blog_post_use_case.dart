abstract class UploadBlogPostUseCase {
  Future<String> execute(String compressedHtmlContent, String userToken);
}
