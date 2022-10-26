from django.db import models

from product.models import Product
from seller.models import Seller
from client.models import Client

class Purchases(models.Model):
    product = models.ForeignKey(
        Product, verbose_name='Produto', on_delete=models.DO_NOTHING)
    seller = models.ForeignKey(
        Seller, related_name='purchases_Seller', on_delete=models.DO_NOTHING)
    client = models.ForeignKey(
        Client, related_name='purchases_Client', on_delete=models.DO_NOTHING)
    qty = models.PositiveSmallIntegerField(verbose_name='Quantidade')
    
    def __str__(self):
        return f'#ID {self.id}'
    