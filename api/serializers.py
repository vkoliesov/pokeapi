from unittest.util import _MAX_LENGTH
from rest_framework import serializers

class PokemonSerializer(serializers.Serializer):
    """Serialize pokemon API"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    url = serializers.CharField(max_length=100)
