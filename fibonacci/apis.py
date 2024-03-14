from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers


# Create your views here.
class FibonacciNumberAPIView(APIView):
    def get(self, request):
        response = {"message": 3}

        return Response(response, status=status.HTTP_200_OK)
