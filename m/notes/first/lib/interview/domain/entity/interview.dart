class Interview {
  final int id;
  final String jobCategory;  // 직무
  final String experienceLevel;  // 경력 수준
  final String createDate;
  final String updateDate;

  Interview({
    this.id = 0,
    this.jobCategory = 'Unknown Category',
    this.experienceLevel = 'Unknown',
    this.createDate = 'Unknown',
    this.updateDate = 'Unknown',
  });

  Map<String, dynamic> toJson() {
    return {
      'interviewId': id,
      'jobCategory': jobCategory,
      'experienceLevel': experienceLevel,
      'createDate': createDate,
      'updateDate': updateDate,
    };
  }

  factory Interview.fromJson(Map<String, dynamic> json) {
    return Interview(
      id: json['interviewId'] ?? 0,
      jobCategory: json['jobCategory'] ?? 'Unknown Category',
      experienceLevel: json['experienceLevel'] ?? 'Unknown',
      createDate: json['createDate'] ?? 'Unknown',
      updateDate: json['updateDate'] ?? 'Unknown',
    );
  }

  @override
  String toString() {
    return 'Interview(id: $id, jobCategory: $jobCategory, experienceLevel: $experienceLevel, createDate: $createDate, updateDate: $updateDate)';
  }
}
