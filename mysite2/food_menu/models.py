from django.db import models

# Create your models here.
class Food(models.Model):
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    item_img = models.ImageField(default="img/food_img.jpg")