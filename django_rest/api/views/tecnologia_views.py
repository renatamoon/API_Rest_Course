from django.http.response import HttpResponse
from rest_framework import response
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