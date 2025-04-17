from abc import ABC, abstractmethod

class InterviewService(ABC):
    @abstractmethod
    def generateInterviewQuestions(self, request: dict) -> dict:
        pass

    @abstractmethod
    def generateFollowupQuestion(self, interviewId: int, questionId: int, answerText: str, userToken: str) -> dict:
        pass
