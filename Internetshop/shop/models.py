from django.db import models

# Create your models here.

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.IntegerField()
    image_Url = models.CharField(max_length=256)

    weight = models.IntegerField(null=True, blank=True)

    model = models.CharField(max_length=64, null=True, blank=True)
    processor = models.CharField(max_length=32, null=True, blank=True)
    ram_size = models.IntegerField(null=True, blank=True)  # размер оперативной памяти
    speed = models.FloatField(null=True, blank=True)  # скорость
    battery_capacity = models.IntegerField(null=True, blank=True)  # ёмкость аккумулятора

    def __str__(self):  #Это кажется для отоброжения имени товара в админки
        return f'{self.name} ID товара: {self.id}  '


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    author = models.CharField(max_length=128)
    rating = models.IntegerField()
    text = models.TextField()

    def __str__(self):
        return f'{self.author}: {self.text[:100]}' #добавляет в админке отоброжение, от кого отзыв
