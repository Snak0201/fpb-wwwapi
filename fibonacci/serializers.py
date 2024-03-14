from rest_framework import serializers


class FibonacciSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=0)
