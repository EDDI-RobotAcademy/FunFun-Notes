class InterviewCreateResponse {
  final int interviewId;

  InterviewCreateResponse({required this.interviewId});

  factory InterviewCreateResponse.fromJson(Map<String, dynamic> json) {
    return InterviewCreateResponse(
      interviewId: json['interviewId'] ?? 0,
    );
  }
}
