from django.db import models

# Create your models here.


class Feira(models.Model):
    nome_feira = models.CharField(max_length=30)
    bairro = models.CharField(max_length=30)
    logradouro = models.CharField(max_length=35)
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    setcens = models.CharField(max_length=16)
    areap = models.CharField(max_length=16)
    cod_dist = models.CharField(max_length=2)
    distrito = models.CharField(max_length=30)
    cod_subpref = models.CharField(max_length=3)
    subpref = models.CharField(max_length=30)
    regiao5 = models.CharField(max_length=10)
    regiao8 = models.CharField(max_length=10)
    registro = models.CharField(max_length=7)
    numero = models.CharField(max_length=14)
    referencia = models.CharField(max_length=45)

    def __str__(self):
        return self.nome_feira
