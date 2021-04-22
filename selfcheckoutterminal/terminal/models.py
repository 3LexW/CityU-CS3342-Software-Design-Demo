from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    pid = models.AutoField("ID", primary_key = True)
    name = models.CharField("Name", max_length = 50)
    age_resticted = models.BooleanField("Is age restricted")
    price = models.FloatField("Price")
    barcode = models.CharField(("Bar Code"), max_length=12)
    imageName = models.CharField(("Image Name"), max_length=50)

    def __str__ (self):
        return self.name

class shoppingCart(models.Model):
    id = models.AutoField("ID", primary_key = True)
    def __str__ (self):
        return self.id

class shoppingCartHistory(models.Model):
    id = models.AutoField("ID", primary_key = True)
    shoppingCart = models.ForeignKey(shoppingCart, verbose_name=("Cart"), on_delete=models.CASCADE)
    item = models.ForeignKey(Product, verbose_name=("Item"), on_delete=models.CASCADE)
    action = models.CharField("Name", max_length = 50)
    activate = models.BooleanField("Activating")