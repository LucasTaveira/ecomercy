from django.db import models

class Address(models.Model):
    street = models.CharField(verbose_name='Rua/Av.', max_length=50)
    city = models.CharField(verbose_name='Cidade', max_length=50)
    number = models.CharField(verbose_name='Numero', max_length=6)
    state = models.CharField(verbose_name='UF', max_length=2)
    district = models.CharField(verbose_name='Bairro', max_length=50)
    reference = models.CharField(verbose_name='Ponto Referencia', max_length=100)
    
    def __str__(self):
        return f'#ID {self.id}, street {self.street}'