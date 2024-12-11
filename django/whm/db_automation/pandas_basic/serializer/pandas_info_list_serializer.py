from rest_framework import serializers

from pandas_basic.entity.pandas_basic_person import PandasBasicPerson


class PandasInfoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PandasBasicPerson
        fields = ['id', 'name', 'age']