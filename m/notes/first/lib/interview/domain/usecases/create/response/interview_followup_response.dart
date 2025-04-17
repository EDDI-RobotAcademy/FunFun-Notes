class InterviewFollowupResponse {
  final int interviewId;
  final int questionId;
  final String question;

  InterviewFollowupResponse({
    required this.interviewId,
    required this.questionId,
    required this.question,
  });

  factory InterviewFollowupResponse.fromJson(Map<String, dynamic> json) {
    return InterviewFollowupResponse(
      interviewId: json['interviewId'],
      questionId: json['questionId'],
      question: json['question'],
    );
  }
}
