import 'package:flutter/cupertino.dart';

class BaseUrlProvider extends ChangeNotifier {
  String _baseUrl;

  BaseUrlProvider(String baseUrl) : _baseUrl = baseUrl;

  String get baseUrl => _baseUrl;

  void setBaseUrl(String url) {
    _baseUrl = url;
    notifyListeners();  // 값이 변경되면 리스너에게 알려줌
  }
}
