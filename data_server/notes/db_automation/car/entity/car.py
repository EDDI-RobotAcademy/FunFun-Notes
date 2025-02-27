from django.db import models

class Car(models.Model):
    url = models.URLField(null=True, blank=True)  # URL 필드는 null과 빈 값 허용
    text = models.CharField(max_length=255, null=True, blank=True)
    drive_range = models.FloatField(null=True, blank=True)
    charge_time = models.FloatField(null=True, blank=True)
    power = models.FloatField(null=True, blank=True)
    전장 = models.IntegerField(null=True, blank=True)  # 차량 길이
    전폭 = models.IntegerField(null=True, blank=True)  # 차량 폭
    전고 = models.IntegerField(null=True, blank=True)  # 차량 높이
    축거 = models.IntegerField(null=True, blank=True)  # 축거 (Wheelbase)

    def __str__(self):
        return f"CarData {self.text} ({self.url})"

    class Meta:
        db_table = 'car'
