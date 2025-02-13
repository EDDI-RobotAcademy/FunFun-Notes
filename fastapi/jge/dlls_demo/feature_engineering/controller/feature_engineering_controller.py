import os
import sys

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

# from feature_engineering.controller.request_form.feature_engineering_request_form import FeatureEngineeringRequestForm
from feature_engineering.service.feature_engineering_service_impl import FeatureEngineeringServiceImpl

# 회귀 알고리즘과 피처 엔지니어링 라우터
featureEngineeringRouter = APIRouter()


#inject 의존성을 주입하는 코드
#Controller는 기본적으로 Service라는 의존성을 가지게 됨
#domain service에 대한 의존성을 주입하는 코드
#단순희 serviceimpl에 대한 코드를 아래와 같이 구성해주면 됨
async def injectFeatureEngineeringService() -> FeatureEngineeringServiceImpl:
    return FeatureEngineeringServiceImpl()

#@featureEngineeringRouter는 APIRouter로 만든 라우터
#post 혹은 get을 이용해서 URL 맵핑을 진행
#async는 비동기 처리
@featureEngineeringRouter.post("/feature-engineering")
async def requestFeatureEngineering(
        # featureEngineeringRequestForm: FeatureEngineeringRequestForm,
                                    featureEngineeringService: FeatureEngineeringServiceImpl =
                                    Depends(injectFeatureEngineeringService)):
    #self.__featureEngineeringSerivce = FeatureEngineeringServiceImpl.getInstance()
    #위 표현(장고)과 아래의 표현은 같은 것을 의미함(엄밀하게 다르지만 우선은 요렇게 파악)
    #featureEngineeringService: FeatureEngineeringServiceImpl =
    #Depends(injectFeatureEngineeringService)):


    featureEngineeringResponse = await featureEngineeringService.featureEngineering()
        # featureEngineeringRequestForm.tofeatureEngineeringRequest())
    comparison = featureEngineeringResponse["comparison"].to_dict(orient="records")

    return {
        "mseError": featureEngineeringResponse["mseError"],
        "comparison": comparison
    }
