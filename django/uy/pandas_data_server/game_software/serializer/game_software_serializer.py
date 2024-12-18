from rest_framework import serializers


class GameSoftwareListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSoftware
        fields = ['id', 'title', 'price', 'image']