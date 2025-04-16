from abc import ABC, abstractmethod

class InterviewService(ABC):
    @abstractmethod
    def generateInterviewQuestions(
        self, interview_id: int, topic: str, experience_level: str, user_token: str
    ) -> dict:
        pass
