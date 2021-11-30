#como a vaga será exibida quando fizermos uma requisicao através do postman
#e como ela será exibida quando for enviada ao banco de dados

from rest_framework import serializers
from ..models import Vaga
from rest_framework.reverse import reverse

class VagaSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Vaga #model de base para verificação se os dados
        #estão validos - no caso somente vamos validar o unico campo que é
        #o nome da Tecnologia - validacao de dados que entrarão no banco de dados
        fields = ('id', 'titulo','descricao', 'salario', 'local', 'quantidade',
        'contato', 'tipo_contratacao', 'tecnologias', 'links', )
    
    
    def get_links(self, obj):
        #obter a requisicao que veio da nossa app
        request = self.context['request']
        #retorna os links para manipular determinada vaga
        return {
             #criando uma rota para o vaga-detalhes
            'self': reverse('vaga-detalhes', kwargs={'id': obj.pk}, request=request),           
            'delete': reverse('vaga-detalhes', kwargs={'id': obj.pk}, request=request),
            'update': reverse('vaga-detalhes', kwargs={'id': obj.pk}, request=request)
        }