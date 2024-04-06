from rest_framework import views, response, status
from random import randint


class SimpleDiceAPIView(views.APIView):
    def post(self, request):
        data = {"value": randint(1, 6)}
        return response.Response(data=data, status=status.HTTP_201_CREATED)