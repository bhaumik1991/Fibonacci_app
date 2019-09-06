import time
from django.shortcuts import render
from django.views import View

from .models import *

def fibonacci(num):
    if num < 2:
        return 1
    else:
        num1 = 1
        num2 = 1
        for i in range(2, num):
            temp = num1 + num2
            num1 = num2
            num2 = temp
        return num2

class FibonacciAPIView(View):
    def get(self,request):
        number = request.GET.get('number')
        if number is None:
            return render(request, 'fibo/index.html')
        else:
            start_time = time.time()
            num = int(number)
            result = fibonacci(num)
            end_time = time.time()
            time_taken = (end_time-start_time)
            print(time_taken)

        query = Fibonacci.objects.create(
            num=num,
            result=result,
            time_taken=time_taken
        )
        query.save()

        data = {
            'num': num,
            'result': result,
            'time_taken': time_taken
        }

        return render(request, 'fibo/index.html', data)
