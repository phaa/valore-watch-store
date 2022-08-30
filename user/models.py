import uuid
from django.db import models

# Produtos e afins
class ProductCategory(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)

class Product(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nome", max_length=100)
    price = models.DecimalField("Preço", max_digits=5, decimal_places=2)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

STATES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )

# Endereços e afins
class State(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("Nome", max_length=2, choices=STATES)


class Address(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    zip = models.IntegerField('Cep')
    public_place = models.CharField('Logradouro', max_length=50)
    number = models.IntegerField('Número')
    complement = models.CharField('Complemento', max_length=100)
    reference = models.CharField('Referência', max_length=100)
    neighborhood = models.CharField('Bairro', max_length=100)
    city = models.CharField('Cidade', max_length=50)
    state = models.CharField("Estado", max_length=2, choices=STATES)
    description = models.CharField('Cidade', max_length=60)
    is_main = models.BooleanField(blank=True)


# Cartões e afins
class CreditCard(models.Model):
    id = models.UUIDField("Id", primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.CharField("Portador", max_length=100)
    number = models.IntegerField("Número do cartão")
    valid_until = models.CharField("Válidade", max_length=20)
    cvv = models.IntegerField("Código de verificação")
