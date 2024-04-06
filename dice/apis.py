from random import randint

from rest_framework import response, status, views

from .serializers import handle_dice_serializer_exception


class SimpleDiceAPIView(views.APIView):
    def get_exception_handler(self):
        return handle_dice_serializer_exception

    def post(self, request):
        data = {"value": randint(1, 6)}
        return response.Response(data=data, status=status.HTTP_201_CREATED)
