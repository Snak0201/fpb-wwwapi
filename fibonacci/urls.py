from django.urls import path

from . import apis

app_name = "fibonacci"

urlpatterns = [path("number", apis.FibonacciNumberAPIView.as_view(), name="number")]
