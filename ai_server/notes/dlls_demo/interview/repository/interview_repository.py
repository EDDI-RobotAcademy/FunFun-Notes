from abc import ABC, abstractmethod
from typing import List

class InterviewRepository(ABC):
    @abstractmethod
    def generateQuestions(
        self, interview_id: int, topic: str, experience_level: str, user_token: str
    ) -> str:
        pass

    @abstractmethod
    def generateFollowupQuestion(
        self, interview_id: int, question_id: int, answer_text: str, user_token: str
    ) -> str:
        pass
