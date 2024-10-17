from django.db import models
from django.urls import reverse


class Produtos(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    image_url = models.CharField(max_length=255)

