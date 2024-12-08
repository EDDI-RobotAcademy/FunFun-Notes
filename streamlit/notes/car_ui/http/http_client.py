import asyncio
import os

import httpx


class HttpClient:
    djangoHttpxInstance = httpx.AsyncClient(
        base_url=os.getenv("DJANGO_URL"),
    )

    @classmethod
    async def post(cls, endpoint: str, data: dict):
        try:
            response = await cls.djangoHttpxInstance.post(endpoint, json=data)

            if response.status_code == 200:
                return True
            else:
                print(f"Failed to send to Django: {response.status_code}")
                return False

        except httpx.RequestError as exc:
            print(f"An error occurred while sending to Django: {str(exc)}")
            return False

    @classmethod
    def post_sync(cls, endpoint: str, data: dict):
        """동기적으로 post 요청을 처리할 수 있도록 래핑"""
        return asyncio.run(cls.post(endpoint, data))

    @classmethod
    async def get(cls, endpoint: str):
        """비동기 GET 요청 처리"""
        try:
            response = await cls.djangoHttpxInstance.get(endpoint)

            if response.status_code == 200:
                return response.json()  # 또는 필요한 다른 데이터 처리
            else:
                print(f"Failed to fetch data from Django: {response.status_code}")
                return None

        except httpx.RequestError as exc:
            print(f"An error occurred while sending GET request: {str(exc)}")
            return None

    @classmethod
    def get_sync(cls, endpoint: str):
        """동기적으로 GET 요청을 처리하는 래핑 메서드"""
        return asyncio.run(cls.get(endpoint))
