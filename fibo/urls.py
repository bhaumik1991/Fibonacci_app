from django.urls import path
from fibo.views import FibonacciAPIView


urlpatterns = [
    path('', FibonacciAPIView.as_view())
]