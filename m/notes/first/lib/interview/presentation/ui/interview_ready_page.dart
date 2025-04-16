import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:first/interview/presentation/providers/interview_create_provider.dart';
import '../../domain/entity/interview.dart';
import '../../interview_module.dart';
import 'interview_start_page.dart'; // InterviewStartPage 임포트

class InterviewReadyPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // InterviewCreateProvider 가져오기
    final createProvider = Provider.of<InterviewCreateProvider>(context);

    return Scaffold(
      appBar: AppBar(
        title: Text('모의 면접 설정'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: InterviewForm(createProvider: createProvider),
      ),
    );
  }
}

class InterviewForm extends StatefulWidget {
  final InterviewCreateProvider createProvider;

  const InterviewForm({Key? key, required this.createProvider}) : super(key: key);

  @override
  _InterviewFormState createState() => _InterviewFormState();
}

class _InterviewFormState extends State<InterviewForm> {
  String? selectedJob;
  String? selectedExperience;

  final Map<String, int> jobOptions = {
    'Backend': 1,
    'Front': 2,
    'DevOps': 3,
    'AI': 4,
    'Embedded': 5,
  };

  final Map<String, int> experienceOptions = {
    '신입': 1,
    '3년 이하': 2,
    '5년 이하': 3,
    '10년 이하': 4,
    '10년 이상': 5,
  };

  void _submitSelection() {
    if (selectedJob != null && selectedExperience != null) {
      final interview = Interview(
        jobCategory: jobOptions[selectedJob!].toString(),
        experienceLevel: experienceOptions[selectedExperience!].toString(),
        createDate: DateTime.now().toString(),
      );

      widget.createProvider.createInterview(interview).then((response) {
        if (widget.createProvider.errorMessage == null && response != null) {
          Navigator.pushReplacement(
            context,
            MaterialPageRoute(
              builder: (context) => InterviewModule.provideInterviewStartPage(
                interviewId: response.interviewId,
                questionId: response.questionId,
                question: response.question,
              ),
            ),
          );
        } else {
          ScaffoldMessenger.of(context).showSnackBar(
            SnackBar(content: Text(widget.createProvider.errorMessage!)),
          );
        }
      });
    } else {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('모든 항목을 선택해주세요.')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        DropdownButtonFormField<String>(
          value: selectedJob,
          hint: Text('직무를 선택하세요'),
          onChanged: (value) => setState(() => selectedJob = value),
          items: jobOptions.keys.map((job) => DropdownMenuItem(
            value: job,
            child: Text(job, style: TextStyle(fontWeight: FontWeight.bold)),
          )).toList(),
        ),
        SizedBox(height: 16),
        DropdownButtonFormField<String>(
          value: selectedExperience,
          hint: Text('경력을 선택하세요'),
          onChanged: (value) => setState(() => selectedExperience = value),
          items: experienceOptions.keys.map((exp) => DropdownMenuItem(
            value: exp,
            child: Text(exp, style: TextStyle(fontWeight: FontWeight.bold)),
          )).toList(),
        ),
        Spacer(),
        Center(
          child: ElevatedButton(
            onPressed: _submitSelection,
            child: Text('시작', style: TextStyle(fontWeight: FontWeight.bold)),
          ),
        ),
      ],
    );
  }
}
