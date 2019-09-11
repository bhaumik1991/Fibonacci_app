from django.db import models
from django.db.models.fields import BigIntegerField


class Fibonacci(models.Model):
    num = models.IntegerField()
    result = models.TextField()
    time_taken = models.CharField(max_length=255)

    def __str__(self):
        return self.num