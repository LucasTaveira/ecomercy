from django.db import models

from product.models import Product
from seller.models import Seller
from client.models import Client


class ItensShoppingCart(models.Model):
    product = models.ForeignKey(Product, verbose_name='Produto', on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, related_name='shoppingart_Client', on_delete=models.CASCADE)
    qty = models.PositiveSmallIntegerField(verbose_name='Quantidade', default=1)
    
class ShoppingCart(models.Model):
    itens_shoppingcart = models.ManyToManyField(ItensShoppingCart)
    value = models.DecimalField(
        verbose_name='Valor Total', max_digits=5, decimal_places=2, default=0)
    
    def __str__(self):
        return f'#ID {self.id}'
    
class Purchases(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='Produto', on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(
        Seller, related_name='purchases_Seller', on_delete=models.DO_NOTHING)
    client = models.ForeignKey(
        Client, related_name='purchases_Client', on_delete=models.DO_NOTHING)
    total_value = models.DecimalField(
        verbose_name='Valor Total', max_digits=5, decimal_places=2, default=0)
    def __str__(self):
        return f'#ID {self.id}'
    