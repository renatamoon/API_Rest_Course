from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from ..services import vagas_service
from ..serializers import vaga_serializer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import vagas
from rest_framework.pagination import LimitOffsetPagination


class VagaList(APIView):
    permission_classes = [IsAuthenticated]
    #com essa permissao, nao podereremos listar nem cadastrar, porém poderemos
    #liustar uma vaga por id.
    def get(self, request, format=None):
        paginacao = LimitOffsetPagination()
        vagas = vagas_service.listar_vagas()
        resultado = paginacao.paginate_queryset(vagas, request)        
        serializer = vaga_serializer.VagaSerializer(resultado, context={'request':request}, many=True)
        return paginacao.get_paginated_response(serializer.data)
        #return Response(Serializer.data, status=status.HTTP_200_OK)

    
    def post(self, request, format=None):
        #passar os dados da req para o serializer para validação dos dados antes de inserir no bd
        serializer = vaga_serializer.VagaSerializer(data=request.data)
        if serializer.is_valid():
            titulo = serializer._validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            salario = serializer.validated_data['salario']
            tipo_contratacao = serializer.validated_data['tipo_contratacao']
            local = serializer.validated_data['local']
            quantidade = serializer.validated_data['quantidade']
            contato = serializer.validated_data['contato']
            tecnologias = serializer.validated_data['tecnologias']
            vaga_nova = vagas.Vaga(titulo=titulo, descricao=descricao, salario=salario
            , tipo_contratacao=tipo_contratacao, local=local, quantidade=quantidade,
            contato=contato, tecnologias=tecnologias)
            vagas_service.cadastrar_vaga(vaga_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #quando inserimos uma info e retorna que foi criado
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #validando de campo em campo
        

class VagaDetalhes(APIView):
    def get(self, request, id, format=None):
        vaga = vagas_service.listar_vaga_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #se retornar todos os detalhes da vaga com o id do paramnetro que
        # mandamos, ele retorna o 200, se nao, retorna o 400.
    
    
    def put(self, request, id, format=None):
        vaga_antiga = vagas_service.listar_vaga_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga_antiga, data=request.data)
        if serializer.is_valid():
            #capiturando os detalhes da requisicao de edição
            titulo = serializer._validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            salario = serializer.validated_data['salario']
            tipo_contratacao = serializer.validated_data['tipo_contratacao']
            local = serializer.validated_data['local']
            quantidade = serializer.validated_data['quantidade']
            contato = serializer.validated_data['contato']
            tecnologias = serializer.validated_data['tecnologias']
            vaga_nova = vagas.Vaga(titulo=titulo, descricao=descricao, salario=salario
            , tipo_contratacao=tipo_contratacao, local=local, quantidade=quantidade,
            contato=contato, tecnologias=tecnologias) #passando todos os atributos
            #responsavel por editar a vaga (no service)
            vagas_service.editar_vaga(vaga_antiga, vaga_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
            #se os dados do serializer forem validos, retorna status 200
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, id, format=None):
        #buscar a vaga para remover a partir do id
        vaga = vagas_service.listar_vaga_id(id)
        vagas_service.remover_vaga(vaga)
        return Response(status=status.HTTP_204_NO_CONTENT)
