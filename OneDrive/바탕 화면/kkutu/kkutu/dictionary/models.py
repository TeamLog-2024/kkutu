from django.db import models
from typing import Any

# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.word