import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';

class InterviewStartPage extends StatefulWidget {
  @override
  _InterviewStartPageState createState() => _InterviewStartPageState();
}

class _InterviewStartPageState extends State<InterviewStartPage> {
  late CameraController _cameraController;
  late List<CameraDescription> cameras;
  bool _isCameraInitialized = false;
  final FlutterTts _flutterTts = FlutterTts();

  @override
  void initState() {
    super.initState();
    _initializeCamera();
    _initializeTTS();
  }

  // 카메라 초기화
  Future<void> _initializeCamera() async {
    cameras = await availableCameras();
    _cameraController = CameraController(cameras[0], ResolutionPreset.medium);
    await _cameraController.initialize();
    setState(() {
      _isCameraInitialized = true;
    });
  }

  // TTS 초기화
  Future<void> _initializeTTS() async {
    await _flutterTts.setLanguage("ko-KR");
    await _flutterTts.setSpeechRate(0.5);
  }

  // 면접 시작 TTS 음성 출력
  Future<void> _speakInterviewStart() async {
    await _flutterTts.speak("지금부터 면접을 진행합니다.");
  }

  @override
  void dispose() {
    _cameraController.dispose();
    _flutterTts.stop();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (!_isCameraInitialized) {
      return Scaffold(
        appBar: AppBar(title: Text('면접 시작')),
        body: Center(child: CircularProgressIndicator()),
      );
    }

    return Scaffold(
      appBar: AppBar(title: Text('면접 시작')),
      body: Center(
        child: Column(
          children: [
            Expanded(
              child: CameraPreview(_cameraController), // 카메라 미리보기
            ),
            ElevatedButton(
              onPressed: () {
                _speakInterviewStart();
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('면접이 시작되었습니다!')),
                );
              },
              child: Text('면접 시작', style: TextStyle(fontSize: 18)),
            ),
          ],
        ),
      ),
    );
  }
}
