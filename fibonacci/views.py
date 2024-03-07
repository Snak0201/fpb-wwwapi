# from django.shortcuts import render
from django.views import View
from django.http.response import JsonResponse

# Create your views here.
class FibonacciView(View):
  def get(self, request):
    data = {"data": "hello"}
    return JsonResponse(data)
