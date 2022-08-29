from turtle import title

from django.db import models


class Address(models.Model):
    zipCode = models.IntegerField('Cep')
    number = models.IntegerField('Número')
    reference = models.CharField('Referência', max_length=100)
    city = models.CharField('Cidade', max_length=50)
    publicPlace = models.CharField('Logradouro', max_length=50)
    district = models.CharField('Bairro', max_length=100)
    state = models.CharField('Estado', max_length=30)
