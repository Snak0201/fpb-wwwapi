# from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import View


# Create your views here.
class FibonacciView(View):
    def get(self, request):
        data = {"data": "hello"}
        return JsonResponse(data)
