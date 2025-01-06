import requests

from db_automation import settings
from payments.repository.payments_repository import PaymentsRepository


class PaymentsRepositoryImpl(PaymentsRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.paymentApiBaseUrl = settings.PAYMENTS_API["PAYMENTS_BASE_URL"]
            cls.__instance.paymentApiKey = settings.PAYMENTS_API["API_KEY"]

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def request(self, paymentRequestData):
        try:
            # API 요청 URL 및 헤더
            url = f"{self.paymentApiBaseUrl}/process"
            headers = {
                "Authorization": f"Bearer {self.paymentApiKey}",
                "Content-Type": "application/json",
            }

            # POST 요청 보내기
            response = requests.post(url, json=paymentRequestData, headers=headers)

            # 응답 상태 코드 확인
            if response.status_code == 200:
                return response.json()  # JSON 응답 반환
            else:
                response.raise_for_status()

        except requests.RequestException as e:
            print(f"결제 API 요청 중 오류 발생: {e}")
            return {"success": False, "message": str(e)}
