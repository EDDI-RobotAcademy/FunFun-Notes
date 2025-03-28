import 'package:camera/camera.dart';
import 'package:flutter/material.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:flutter_sound/flutter_sound.dart'; // Used for audio recording
import 'package:path_provider/path_provider.dart';
import 'package:speech_to_text/speech_to_text.dart' as stt; // Speech to Text 라이브러리 추가
import 'dart:io';
import 'package:permission_handler/permission_handler.dart'; // 권한 요청 패키지

class InterviewStartPage extends StatefulWidget {
  @override
  _InterviewStartPageState createState() => _InterviewStartPageState();
}

class _InterviewStartPageState extends State<InterviewStartPage> {
  late CameraController _cameraController;
  late List<CameraDescription> cameras;
  bool _isCameraInitialized = false;
  final FlutterTts _flutterTts = FlutterTts();
  FlutterSoundRecorder _recorder = FlutterSoundRecorder();
  bool _isRecording = false;
  String _audioFilePath = '';
  stt.SpeechToText _speechToText = stt.SpeechToText(); // 음성 인식 객체
  bool _isListening = false; // 음성 인식 상태
  String _recognizedText = ''; // 변환된 텍스트 저장

  @override
  void initState() {
    super.initState();
    _requestPermissions();  // 권한 요청
    _initializeCamera();
    _initializeTTS();
    _initializeAudioRecorder();
    _initializeSpeechToText(); // 음성 인식 초기화
  }

  // 권한 요청 함수
  Future<void> _requestPermissions() async {
    // 마이크 권한 요청
    PermissionStatus microphonePermission = await Permission.microphone.request();
    if (!microphonePermission.isGranted) {
      print("마이크 권한이 필요합니다.");
      return;
    }

    // 카메라 권한 요청
    PermissionStatus cameraPermission = await Permission.camera.request();
    if (!cameraPermission.isGranted) {
      print("카메라 권한이 필요합니다.");
      return;
    }

    // 권한이 모두 승인되었을 때 처리
    print("모든 권한이 승인되었습니다.");
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

  // Audio Recorder 초기화
  Future<void> _initializeAudioRecorder() async {
    final directory = await getApplicationDocumentsDirectory();
    _audioFilePath = '${directory.path}/interview_audio.wav';
    await _recorder.openRecorder();
  }

  // 음성 인식 초기화
  Future<void> _initializeSpeechToText() async {
    bool available = await _speechToText.initialize();
    if (available) {
      setState(() {
        _isListening = false;
      });
    }
  }

  // 면접 시작 TTS 음성 출력
  Future<void> _speakInterviewStart() async {
    await _flutterTts.speak("지금부터 면접을 진행하겠습니다.");
  }

  // 음성 녹음 시작/종료
  Future<void> _toggleRecording() async {
    if (_isRecording) {
      await _recorder.stopRecorder();
      setState(() {
        _isRecording = false;
      });
      // 서버로 녹음된 오디오 파일 전송
      _sendAudioToServer();
    } else {
      await _recorder.startRecorder(toFile: _audioFilePath);
      setState(() {
        _isRecording = true;
      });
    }
  }

  // 음성 인식 시작
  void _startListening() {
    _speechToText.listen(
      onResult: (result) {
        setState(() {
          _recognizedText = result.recognizedWords;
        });
        print("인식된 텍스트: $_recognizedText");
      },
      listenFor: Duration(seconds: 30),  // 30초 동안 듣기
      pauseFor: Duration(seconds: 5),    // 5초 동안 말하지 않으면 자동으로 멈추기
      partialResults: true,              // 부분 결과도 받아오기
      localeId: "ko_KR",                 // 한국어로 설정
      onSoundLevelChange: (level) {
        print("음성 레벨: $level");
      },
    );
    setState(() {
      _isListening = true;
    });
  }

  // 음성 인식 종료
  void _stopListening() {
    _speechToText.stop();
    setState(() {
      _isListening = false;
    });
    // 서버로 변환된 텍스트 전송
    _sendRecognizedTextToServer();
  }

  // 녹음한 음성을 서버에 전송
  Future<void> _sendAudioToServer() async {
    await Future.delayed(Duration(seconds: 2));
    String responseText = "면접이 종료되었습니다! 수고하셨습니다.";
    await _flutterTts.speak(responseText);
  }

  // 음성 인식된 텍스트 서버로 전송
  Future<void> _sendRecognizedTextToServer() async {
    print("인식된 텍스트: $_recognizedText");
    // 여기서 변환된 텍스트를 서버로 전송하는 로직을 추가하세요.
    // 예: HTTP 요청으로 서버에 텍스트를 보내는 코드
  }

  @override
  void dispose() {
    _cameraController.dispose();
    _flutterTts.stop();
    if (_isRecording) {
      _recorder.stopRecorder();
    }
    _recorder.closeRecorder();
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
              child: CameraPreview(_cameraController),
            ),
            ElevatedButton(
              onPressed: () async {
                await _speakInterviewStart();  // 면접 시작 음성 출력
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(content: Text('면접이 시작되었습니다! 질문을 시작하겠습니다!')),
                );
                _toggleRecording();  // 음성 녹음 시작/종료
              },
              child: Text(_isRecording ? '녹음 종료' : '면접 시작', style: TextStyle(fontSize: 18)),
            ),
            ElevatedButton(
              onPressed: _isListening ? _stopListening : _startListening,
              child: Text(_isListening ? '음성 인식 종료' : '답변 시작'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // 답변 완료 버튼이 눌리면 텍스트 전송
                _sendRecognizedTextToServer();
              },
              child: Text('답변 완료'),
            ),
            SizedBox(height: 20),
            Text('인식된 텍스트: $_recognizedText'),
          ],
        ),
      ),
    );
  }
}
