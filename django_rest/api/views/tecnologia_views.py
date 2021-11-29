from django.http.response import HttpResponse
from rest_framework import response, serializers
from rest_framework.views import APIView
from ..services import tecnologia_service
from ..serializers import tecnologia_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import tecnologia

class TecnologiaList(APIView):
    #comporta os metodos que nao precisam de parametros para funcionar
    #neste caso está listando tecnologias, ele nao precisa de um ID para retornar
    def get(self, request, format=None):
        tecnologias = tecnologia_service.listar_tecnologias()
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #quando uma requisicao da correta ela retorna statuscode 200

    def post(self, request, format=None):
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_bd = tecnologia_service.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED) #QUE CONSEGUIU
            #INSERIR ALGO NO BANCO DE DADOS
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TecnologiaDetalhes(APIView):
    def get(self, request, id, format=None): #recebe uma requisicao + id e atributo
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia)
        return Response(serializer.data, status=status.HTTP_200_OK)
         #caso a tecnologia for retornada na parte de services, ela passa por essa
         #validação para retornara a tecologia por ID + serializer

    
    def put(self, request, id, format=None):
        #busca a tec por id do bd e passa os dados da requisicao para o serializer
        # para que sejam validados antes de fazer alguma alteracao e depois editar
        tecnologia_antiga = tecnologia_service.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia_antiga, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_service.editar_tecnologia(tecnologia_antiga, tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        tecnologia = tecnologia_service.listar_tecnologia_id(id)
        tecnologia_service.remover_tecnologia(tecnologia)
        return Response(status=status.HTTP_204_NO_CONTENT)
        #quando ela recebe esse verbo 204, ela tem que saber que essa 
        #tecnologia foi removida com sucesso
        