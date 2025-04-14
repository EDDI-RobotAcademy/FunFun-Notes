import 'package:flutter/material.dart';
import '../../../domain/entity/interview.dart';

class InterviewItem extends StatelessWidget {
  final Interview interview;

  const InterviewItem({
    Key? key,
    required this.interview,
  }) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 16),
      elevation: 4,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(12),
      ),
      child: ListTile(
        contentPadding: const EdgeInsets.all(16),
        subtitle: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            SizedBox(height: 8),
            Text(
              '직무: ${interview.jobCategory}',
              style: TextStyle(fontSize: 16, color: Colors.grey[600]),
            ),
            Text(
              '경력: ${interview.experienceLevel}',
              style: TextStyle(fontSize: 16, color: Colors.grey[600]),
            ),
            Text(
              '업데이트 날짜: ${interview.updateDate}',
              style: TextStyle(fontSize: 16, color: Colors.grey[600]),
            ),
          ],
        ),
        trailing: Icon(Icons.arrow_forward_ios),
        onTap: () {
          // Navigate to detailed page or handle action on tap
        },
      ),
    );
  }
}
