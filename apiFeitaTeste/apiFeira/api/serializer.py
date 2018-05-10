from rest_framework import serializers
from .models import *


class FeiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feira
        fields = ['id', 'nome_feira', 'bairro', 'logradouro', 'longitude', 'latitude',
                  'setcens', 'areap', 'cod_dist', 'distrito', 'cod_subpref', 'subpref',
                  'regiao5', 'regiao8', 'registro', 'numero', 'referencia']
