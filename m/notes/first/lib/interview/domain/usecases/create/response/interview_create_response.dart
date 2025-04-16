class InterviewCreateResponse {
  final int interviewId;
  final int questionId;
  final String question;

  InterviewCreateResponse({
    required this.interviewId,
    required this.questionId,
    required this.question,
  });

  factory InterviewCreateResponse.fromJson(Map<String, dynamic> json) {
    return InterviewCreateResponse(
      interviewId: json['interviewId'] ?? 0,
      questionId: json['questionId'] ?? 0,
      question: json['question']?.toString() ?? '',
    );
  }
}
