from typing import List
from interview.repository.interview_repository import InterviewRepository

class InterviewRepositoryImpl(InterviewRepository):
    def generateQuestions(
        self, interview_id: int, topic: str, experience_level: str, user_token: str
    ) -> str:
        print(f"📡 [repository] Generating a single question from fine-tuned model for interviewId={interview_id}, userToken={user_token}")

        # TODO: OpenAI 연동 or 파인튜닝 모델로 대체
        return (
            f"{topic} 분야에서 최근 관심 있게 본 트렌드는 무엇이며, "
            f"그에 관련한 본인의 경험을 말씀해주시고, "
            f"{experience_level} 수준에서 마주치는 대표적인 문제는 무엇이라 생각하시나요?"
        )

    def generateFollowupQuestion(
            self, interview_id: int, question_id: int, answer_text: str, user_token: str
    ) -> str:
        print(f"📡 [repository] Generating follow-up question for interviewId={interview_id}, questionId={question_id}")

        # TODO: OpenAI 연동 or 파인튜닝 모델로 대체
        return (
            "이전에 말씀하신 경험 중 가장 어려웠던 상황은 무엇이었고, "
            "그 상황을 어떻게 극복하셨는지 자세히 말씀해 주세요."
        )
