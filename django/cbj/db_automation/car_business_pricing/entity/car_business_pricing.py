from django.db import models

class CarBusinessPricing(models.Model):
    id = models.AutoField(primary_key=True)
    사업자 = models.CharField(max_length=50, null=True, blank=True)
    로밍평균요금 = models.FloatField(null=True, blank=True)
    회원평균요금 = models.FloatField(null=True, blank=True)
    비회원평균요금 = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.사업자} Pricing"

    class Meta:
        db_table = 'car_business_pricing'
