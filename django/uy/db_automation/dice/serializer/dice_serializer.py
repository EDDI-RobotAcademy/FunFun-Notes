from rest_framework import serializers

from db_automation.dice.entity.dice import Dice

class DiceSerializer(serializers.ModelSerializer):
    # serializers.ModelSerializer를 상속하여 DiceSerializer를 정의함
    class Meta:
        # DiceSerializer의 동작 방식을 정의합니다.
        model = Dice
        # 이 직렬화기가 다룰 모델을 지정 : 그게 Dice
        fields = ['id', 'number']
        # JSON 데이터에서 id와 number 필드만 포함됨