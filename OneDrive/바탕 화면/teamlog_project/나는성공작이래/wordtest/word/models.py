from django.db import models
from typing import Any

# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=50, null=True)
    mean = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.word