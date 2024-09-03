from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=10, decimal_places=2)

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

class Carrinho(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    produtos = models.ManyToManyField(Product, through='CarrinhoProduto')

class CarrinhoProduto(models.Model):
    carrinho = models.ForeignKey(Carrinho, on_delete=models.CASCADE)
    produto = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.quantidade > self.produto.stock:
            raise ValueError("Not enough stock for this product")
        super().save(*args, **kwargs)