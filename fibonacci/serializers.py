from rest_framework import serializers
from rest_framework.views import exception_handler

def handle_fibonacci_serializer_exception(exc, context):
    response = exception_handler(exc, context)

    if response:
        response.data["value"] = None
        response.exc = exc
    return response

class FibonacciSerializer(serializers.Serializer):
    number = serializers.IntegerField(min_value=0)
