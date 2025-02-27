import 'dart:convert';
import 'dart:typed_data';

import 'package:flutter/services.dart';
import 'package:crypto/crypto.dart';
import 'package:convert/convert.dart';

Future<void> printKeyHash() async {
  try {
    final ByteData keyStore =
    await rootBundle.load('assets/android/app/debug.keystore');

    final Uint8List keyBytes = keyStore.buffer.asUint8List();
    final Digest sha1Digest = sha1.convert(keyBytes);

    String keyHash = base64.encode(sha1Digest.bytes);
    print('🔑 현재 앱 Key Hash: $keyHash');
  } catch (e) {
    print('❌ Key Hash 계산 중 오류 발생: $e');
  }
}
