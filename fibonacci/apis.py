from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import FibonacciSerializer, handle_fibonacci_serializer_exception

# Create your views here.
class FibonacciNumberAPIView(APIView):
    def get_exception_handler(self):
        return handle_fibonacci_serializer_exception

    def get(self, request):
        n = request.query_params.get("n")
        serializer = FibonacciSerializer(data={"n": n})
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        response = {"value": serializer.validated_data.get("n")}

        return Response(response, status=status.HTTP_200_OK)
