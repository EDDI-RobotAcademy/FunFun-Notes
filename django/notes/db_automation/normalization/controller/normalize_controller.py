from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.status import HTTP_200_OK

import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
# pip install scikit-learn

class NormalizeController(viewsets.ViewSet):

    def requestNormalize(self, request):
        print(f"데이터 준비")
        data = {
            'Age': [25, 30, 35, None, 40],
            'Salary': [50000, 60000, None, 80000, 90000],
            'Experience': [1, 5, 10, 15, 20]
        }
        
        # 판다스라고 부르는 패키지로 데이터를 구성함(엑셀처럼 Age 열, Salary  열, Experience 열을 구성)
        df = pd.DataFrame(data)
        print("Original Data:")
        print(df)

        # fillna는 결측치(NaN) -> Not a Number를 특정 값으로 채우기 위해 제공함
        # 아래 케이스의 경우 Age의 평균 값으로 숫자가 아닌 빈 공간을 채움
        # 위의 data를 보면 None 부분을 평균으로 채우겠다는 뜻
        print(f"결측치 처리 -> 평균값으로 대체")
        df['Age'].fillna(df['Age'].mean(), inplace=True)
        # Salary의 경우 median이 있는데 median은 중간값이라고 해서
        # 어떤 값이던 실제 정말 가운데 위치한 값을 배치함 (평균이 아님)
        df['Salary'].fillna(df['Salary'].median(), inplace=True)

        print("\nData After Handling Missing Values:")
        print(df)

        print(f"Min-Max Scaling 정규화")
        # MinMaxScaler의 경우 최소값과 최대값을 기준으로 스케일하기 위한 녀석임
        # 최소값, 최대값으로 구성해서 쉽게 스케일 하도록 만듬
        # 아래의 StandardScaler를 통해서 0 ~ 1 사이로 정규화(표준화)함
        scaler = MinMaxScaler()
        # 스케일을 적용한 숫자값으로 환산 (scaler.fit_transform)
        df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

        print("\nData After Min-Max Scaling:")
        print(df_scaled)
        
        print("표준화")
        # 위에 논했듯이 0 ~ 1 사이로 정리하는 부분 (standard_scaler.fit_transform)
        standard_scaler = StandardScaler()
        df_standardized = pd.DataFrame(standard_scaler.fit_transform(df), columns=df.columns)

        print("\nData After Standard Scaling:")
        print(df_standardized)

        return JsonResponse({"data": df_standardized.to_dict()}, status=status.HTTP_200_OK)
