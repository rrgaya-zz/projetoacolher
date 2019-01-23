from django.db import models
from django.utils import timezone

# Create your models here.
class CargoDirigente(models.Model):
    """Cargos da diretoria da instituição"""
    cargo = models.CharField(
        max_length=100
    )
    def __str__(self):
        return self.cargo

class Dirigente(models.Model):
    """Dirigentes da Instituição"""
    nome = models.CharField(
        max_length=100,
        null=False,
        blank=False

    )

    cpf = models.CharField(
        max_length=10,
        null=False,
        blank=False
    )

    cargo = models.ForeignKey(
        CargoDirigente,
        models.DO_NOTHING
    )
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):

    cpf = models.CharField(
        max_length=10,
        null=False,
        blank=False
        )

    cnpj = models.CharField(
        max_lenght=14,
        null=True,
        blank=False
    )

    cpf = models.CharField(
        max_lenght=11,
        null=True,
        blank=True
    )

    rua = models.CharField(
        max_lenght=200,
        null=False,
        blank=False
    )

    bairro = models.CharField(
        max_lenght=100,
        null=False,
        blank=False
    )

    numero = models.CharField(
        max_lenght=6,
        null=False,
        blank=False
    )
    def __str__(self):
        return self.razao
