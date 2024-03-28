from rest_framework import serializers
from rest_framework.views import exception_handler


def handle_fibonacci_serializer_exception(exc, context):
    response = exception_handler(exc, context)

    if response:
        error = {}

        for key, value in response.data.items():
            error[key] = value

        # NOTE: 元々のエラーは削除してレスポンスを組みなおす
        response.data.clear()

        response.data["value"] = None
        response.data["errors"] = error
        response.exc = exc
    return response


class FibonacciSerializer(serializers.Serializer):
    n = serializers.IntegerField(min_value=0)
