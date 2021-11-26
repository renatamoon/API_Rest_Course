#como a tecnologia será exibida quando fizermos uma requisicao através do postman
#e como ela será exibida quando for enviada ao banco de dados

from rest_framework import serializers
from ..models import Tecnologia

class TecnologiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologia #model de base para verificação se os dados
        #estão validos - no caso somente vamos validar o unico campo que é
        #o nome da Tecnologia - validacao de dados que entrarão no banco de dados
        fields = ('nome', )