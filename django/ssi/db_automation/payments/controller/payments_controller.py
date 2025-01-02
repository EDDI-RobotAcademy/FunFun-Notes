from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status


from redis_cache.service.redis_cache_service_impl import RedisCacheServiceImpl


class PaymentsController(viewsets.ViewSet):
    redisCacheService = RedisCacheServiceImpl.getInstance()
    paymentsService = PaymentsServiceImpl.getInstance()

    def requestProcessPayments(self, request):
        postRequest = request.data
        selectedItems = postRequest.get("items")
        userToken = postRequest.get("userToken")

        if not userToken:
            return JsonResponse({"error": "userToken이 필요합니다", "success": False}, status=status.HTTP_400_BAD_REQUEST)

        if not selectedItems or not isinstance(selectedItems, list):
            return JsonResponse(
                {"error": "유효한 상품 목록이 필요합니다", "success": False},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            accountId = self.redisCacheService.getValueByKey(userToken)
            if not accountId:
                return JsonResponse(
                    {"error": "유효하지 않은 userToken입니다", "success": False},
                    status=status.HTTP_401_UNAUTHORIZED,
                )

            paymentResult = self.paymentsService.process(accountId, selectedItems)

            if paymentResult is not None:
                # 결제 성공 시 성공 URL 반환
                return JsonResponse(
                    {
                        "success": True,
                        "message": "결제가 성공적으로 처리되었습니다.",
                        "paymentUrl": paymentResult["paymentUrl"],  # 결제 URL
                        "paymentsId": paymentResult["paymentsId"],  # 결제 ID
                    },
                    status=status.HTTP_200_OK,
                )
            else:
                return JsonResponse(
                    {"error": "결제 처리 중 오류 발생", "success": False},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )

        except Exception as e:
            # 서버 내부 오류 처리
            print(f"주문 처리 중 오류 발생: {e}")
            return JsonResponse(
                {"error": "서버 내부 오류", "success": False},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
