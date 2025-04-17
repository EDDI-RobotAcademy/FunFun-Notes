from pydantic import BaseModel

class QuestionGenerationAfterAnswerRequestForm(BaseModel):
    userToken: str
    interviewId: int
    questionId: int
    answerText: str
