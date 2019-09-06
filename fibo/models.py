from  django.db import models

class Fibonacci(models.Model):
    num = models.IntegerField()
    result = models.PositiveIntegerField()
    time_taken = models.CharField(max_length=255)

    def __str__(self):
        return self.num