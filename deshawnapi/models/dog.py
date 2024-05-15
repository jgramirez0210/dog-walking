from django.db import models
from .walker import Walker

class Dog(models.Model):
    name = models.CharField(max_length=155)
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE, related_name='dogs')

