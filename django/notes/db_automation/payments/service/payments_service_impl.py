from payments.repository.payments_repository_impl import PaymentsRepositoryImpl
from payments.service.payments_service import PaymentsService


class PaymentsServiceImpl(PaymentsService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__paymentsRepository = PaymentsRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def process(self, accountId, selectedItems):
        try:
            # 결제 요청 데이터 생성
            paymentRequestData = {
                "accountId": accountId,
                "items": selectedItems,
                "totalAmount": sum(item["price"] * item["quantity"] for item in selectedItems),
            }

            # PaymentsRepository를 통해 외부 결제 API 요청
            paymentResponse = self.__paymentsRepository.request(paymentRequestData)

            # 결제 요청 성공 여부 확인
            if paymentResponse["success"]:
                return {
                    "paymentUrl": paymentResponse["paymentUrl"],
                    "paymentsId": paymentResponse["paymentsId"],
                }
            else:
                raise Exception(f"결제 실패: {paymentResponse.get('message', '알 수 없는 오류')}")

        except Exception as e:
            print(f"PaymentsServiceImpl.process 오류: {e}")
            raise
    