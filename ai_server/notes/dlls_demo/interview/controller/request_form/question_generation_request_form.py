from pydantic import BaseModel

class QuestionGenerationRequestForm(BaseModel):
    interviewId: int
    topic: str
    experienceLevel: str
    userToken: str
