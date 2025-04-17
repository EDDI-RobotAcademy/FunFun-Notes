from interview.service.interview_service import InterviewService
from interview.repository.interview_repository_impl import InterviewRepositoryImpl
from interview.service.request.question_generation_request import QuestionGenerationRequest


class InterviewServiceImpl(InterviewService):
    def __init__(self):
        self.interviewRepository = InterviewRepositoryImpl()

    def generateInterviewQuestions(self, request: QuestionGenerationRequest) -> dict:
        interviewId = request.interviewId
        topic = request.topic
        experienceLevel = request.experienceLevel
        userToken = request.userToken

        print(f"💡 [service] Requesting question generation for interviewId={interviewId}")

        questions = self.interviewRepository.generateQuestions(
            interviewId, topic, experienceLevel, userToken
        )

        return {
            "interviewId": interviewId,
            "questions": questions
        }

    def generateFollowupQuestion(
            self, interview_id: int, question_id: int, answer_text: str, user_token: str
    ) -> dict:
        print(f"💡 [service] Requesting follow-up question for interviewId={interview_id}, questionId={question_id}")

        followup_question = self.interviewRepository.generateFollowupQuestion(
            interview_id, question_id, answer_text, user_token
        )

        return {
            "interviewId": interview_id,
            "questions": followup_question
        }

