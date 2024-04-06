from django.urls import path

from . import apis

app_name = "dice"

urlpatterns = [path("simple", apis.SimpleDiceAPIView.as_view(), name="simple")]
