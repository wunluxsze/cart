from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.IntegerField()

class Cart(models.Model):
    products = models.ManyToManyField(Products)