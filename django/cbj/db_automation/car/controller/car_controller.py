from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets, status

from car.service.car_service_impl import CarServiceImpl


class CarController(viewsets.ViewSet):
    __carService = CarServiceImpl.getInstance()

    def requestCrawlCarData(self, request):
        isSuccess = self.__carService.crawlCarData()

        return JsonResponse({'success': isSuccess})

    def requestCarList(self, request):
        try:
            carListDataFrame = self.__carService.carList()
            print(f"carListDataFrame: {carListDataFrame}")

            return JsonResponse(carListDataFrame.to_dict(orient='records'), safe=False)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def requestModifyCarText(self, request):
        isSuccess = self.__carService.requestModifyCarText()

        if isSuccess:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Failed to modify car text'},
                                status=status.HTTP_400_BAD_REQUEST)

