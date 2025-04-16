from interview.service.interview_service import InterviewService
from interview.repository.interview_repository_impl import InterviewRepositoryImpl

class InterviewServiceImpl(InterviewService):
    def __init__(self):
        self.interviewRepository = InterviewRepositoryImpl()

    def generateInterviewQuestions(
        self, interview_id: int, topic: str, experience_level: str, user_token: str
    ) -> dict:
        print(f"💡 [service] Requesting question generation for interviewId={interview_id}")

        questions = self.interviewRepository.generateQuestions(
            interview_id, topic, experience_level, user_token
        )

        return {
            "interviewId": interview_id,
            "questions": questions
        }
