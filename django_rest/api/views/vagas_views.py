from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from ..services import vagas_service
from ..serializers import vaga_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import Vaga

class VagaList(APIView):
    def get(self, request, format=None):
        vagas = vagas_service.listar_vagas()
        Serializer = vaga_serializer.VagaSerializer(vagas, many=True)
        return Response(Serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, format=None):
        #passar os dados da req para o serializer para validação dos dados antes de inserir no bd
        serializer = vaga_serializer.VagaSerializer(data=request.data)
        if serializer.is_valid():
            titulo = serializer._validated_data['titulo']
            descricao = serializer.validate_data['descricao']
            salario = serializer.validate_data['salario']
            tipo_contratacao = serializer.validate_data['tipo_contratacao']
            local = serializer.validate_data['local']
            quantidade = serializer.validate_data['quantidade']
            contato = serializer.validate_data['contato']
            tecnologias = serializer.validate_data['tecnologias']

    