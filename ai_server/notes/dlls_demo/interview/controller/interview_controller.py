from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from interview.service.interview_service_impl import InterviewServiceImpl

from interview.controller.request_form.question_generation_request_form import QuestionGenerationRequestForm

interviewRouter = APIRouter()


# 의존성 주입
async def injectInterviewService() -> InterviewServiceImpl:
    return InterviewServiceImpl()

@interviewRouter.post("/interview/question/generate")
async def generateInterviewQuestion(
    requestForm: QuestionGenerationRequestForm,
    interviewService: InterviewServiceImpl = Depends(injectInterviewService)
):
    print(f"🎯 [controller] Received generateInterviewQuestion() requestForm: {requestForm}")

    try:
        # 여기에 질문 생성 로직 호출
        response = interviewService.generateInterviewQuestions(
            requestForm.interviewId,
            requestForm.topic,
            requestForm.experienceLevel,
            requestForm.userToken
        )

        return JSONResponse(
            content=response,
            status_code=status.HTTP_200_OK,
            headers={"Content-Type": "application/json; charset=UTF-8"}
        )

    except Exception as e:
        print(f"❌ Error in generateInterviewQuestion(): {str(e)}")
        raise HTTPException(status_code=500, detail="서버 내부 오류 발생")
