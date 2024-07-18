from django.db import models

# Create your models here.

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_Url = models.CharField(max_length=256)

    def __str__(self):
        return f'{self.name}'
