from car_business_pricing.entity.car_business_pricing import CarBusinessPricing
from car_business_pricing.repository.car_business_pricing_repository import CarBusinessPricingRepository

import pandas as pd


class CarBusinessPricingRepositoryImpl(CarBusinessPricingRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, carBusinessPricingData):
        carBusinessPricing = CarBusinessPricing(**carBusinessPricingData)
        carBusinessPricing.save()
        return carBusinessPricing

    def createMany(self, carBusinessPricingDataList):
        carBusinessPricingList = []
        for carBusinessPricingData in carBusinessPricingDataList:
            carBusinessPricing = CarBusinessPricing(**carBusinessPricingData)
            carBusinessPricing.save()
            carBusinessPricingList.append(carBusinessPricing)

        return carBusinessPricingList

    def findAll(self):
        carBusinessPricingList = CarBusinessPricing.objects.all().values()
        print(f"carBusinessPricingList: {carBusinessPricingList}")
        return pd.DataFrame(carBusinessPricingList)
