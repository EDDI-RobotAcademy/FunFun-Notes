from rset_framework import serializers


class GameSoftwareListSerializer(serializers.modelserializer):
    class meta:
        model = GameSoftware
        fields = ['id', 'title', 'price', 'image']