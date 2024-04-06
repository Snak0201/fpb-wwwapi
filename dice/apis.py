from random import randint

from rest_framework import response, status, views


class SimpleDiceAPIView(views.APIView):
    def post(self, request):
        data = {"value": randint(1, 6)}
        return response.Response(data=data, status=status.HTTP_201_CREATED)
