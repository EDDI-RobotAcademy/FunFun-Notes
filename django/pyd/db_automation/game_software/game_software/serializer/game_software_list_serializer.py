from rest_framework import serializers

from game_software.entity.game_software import GameSoftware


class GameSoftwareListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameSoftware
        fields = ['id', 'title', 'price', 'image']