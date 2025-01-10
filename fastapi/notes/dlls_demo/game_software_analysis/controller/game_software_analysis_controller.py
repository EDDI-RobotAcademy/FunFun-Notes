import os
import sys

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from fastapi.responses import JSONResponse, FileResponse
from typing import Any

from game_software_analysis.service.game_software_analysis_service_impl import GameSoftwareAnalysisServiceImpl

gameSoftwareAnalysisRouter = APIRouter()

async def injectGameSoftwareAnalysisService() -> GameSoftwareAnalysisServiceImpl:
    return GameSoftwareAnalysisServiceImpl()

@gameSoftwareAnalysisRouter.post("/game-software-data/analysis")
async def requestGameSoftwareAnalysis(file: UploadFile = File(...),
                                      gameSoftwareAnalysisService: GameSoftwareAnalysisServiceImpl =
                                      Depends(injectGameSoftwareAnalysisService)):

    if file.content_type not in ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                 "application/vnd.ms-excel"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Please upload an Excel file."
        )

    currentDirectory = os.getcwd()
    print(f"Current working directory: {currentDirectory}")
    resourceDirectory = os.path.join(currentDirectory, "resource")

    filePath = os.path.join(resourceDirectory, file.filename)
    with open(filePath, "wb") as temporaryFile:
        temporaryFile.write(await file.read())

    try:
        gameSoftwareAnalysisResponse = await gameSoftwareAnalysisService.requestAnalysis(filePath)

        # 그래프 이미지 파일 경로
        graphImagePath = os.path.join(currentDirectory, "resource", "age_group_purchase_cost.png")

        # 그래프가 존재하면 이미지 파일을 클라이언트로 전송
        if os.path.exists(graphImagePath):
            return FileResponse(graphImagePath, headers={"X-Response-Type": "image"})

        return JSONResponse(content=gameSoftwareAnalysisResponse)

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An error occurred while processing the file: {str(e)}"
        )
    finally:
        if os.path.exists(filePath):
            os.remove(filePath)
