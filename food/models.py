from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=500, default='https://livingstonbagel.com/wp-content/uploads/2016/11/food-placeholder.jpg')

    def __str__(self):
        return self.name
