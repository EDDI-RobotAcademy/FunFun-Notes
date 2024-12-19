import os
import sys


from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

# from feature_engineering.controller.request_form.feature_engineering_request_form import FeatureEngineeringRequestForm
from feature_engineering.service.feature_engineering_service_impl import FeatureEngineeringServiceImpl

# 회귀 알고리즘과 피처 엔지니어링 라우터
featureEngineeringRouter = APIRouter()

async def injectFeatureEngineeringService() -> FeatureEngineeringServiceImpl:
    return FeatureEngineeringServiceImpl()

@featureEngineeringRouter.post("/feature-engineering")
async def requestFeatureEngineering(
        # featureEngineeringRequestForm: FeatureEngineeringRequestForm,
                                    featureEngineeringService: FeatureEngineeringServiceImpl =
                                    Depends(injectFeatureEngineeringService)):

    featureEngineeringResponse = await featureEngineeringService.featureEngineering()
        # featureEngineeringRequestForm.tofeatureEngineeringRequest())

    return featureEngineeringResponse