from django.db import models

from seller.models import Seller

class Product(models.Model):
    name = models.CharField(verbose_name='Nome Produto', max_length=50)
    description = models.TextField(verbose_name='Descrição Produto')
    picture = models.ImageField(
        verbose_name='Foto produto', upload_to='media/product/pictures/')
    value = models.DecimalField(
        verbose_name='Valor Produto', max_digits=5, decimal_places=2)
    seller = models.ForeignKey(
        Seller, verbose_name='Vendedore', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'#ID {self.id}, name {self.name}'