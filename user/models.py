import uuid

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


# Create your models here.
class CreditCard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField("Portador", max_length=100)
    number = models.IntegerField("Número do cartão")
    valid_until = models.DateField("Válido até")
    cvv = models.IntegerField("Código de verificação")

    class Meta:
        db_table = "credit_card"
