# Serializer: 밑에 적혀있는 항목의 데이터만 뽑아 내겠다는 뜻
from rest_framework import serializers
from pandas_basic.entity.pandas_basic_person import PandasBasicPerson


class PandasInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PandasBasicPerson
        fields = ['id', 'name', 'age']

