from django.http.response import Http404
from ..models import Tecnologia, Vaga
from .tecnologia_service import listar_tecnologia_id

def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas
    #buscar as vagas dentro do banco de dados

def cadastrar_vaga(vaga):
    vaga_bd = Vaga.objects.create(titulo=vaga.titulo, descricao=vaga.descricao,
    salario=vaga.salario, tipo_contratacao=vaga.tipo_contratacao, 
    local=vaga.local, quantidade=vaga.quantidade, contato=vaga.contato)
    #tecnologias nao entra, porque teremso que fazer o relacionamento
    #possa ser que o user passe mais de uma tecnologia
    vaga_bd.save()
    #pegar a vaga e relacionar com todas as tecnologias
    for vaga in vaga.tecnologias:
        tecnologia = listar_tecnologia_id(vaga.id)
        vaga_bd.tecnologias.add(tecnologia) #relacionando de n pra n
        # a tecnologia a essa vaga_bd
        #criaremos um vaga com base em todas as infos   
        return vaga_bd  

def listar_vaga_id(id):
    try:
        return Vaga.objects.get(id=id) #se existir uma vaga com este ID
    except Vaga.DoesNotExist:
        raise Http404 #vamos usar este mesmo metoodo para outras funcionalidades

    
def editar_vaga(vaga_antiga, vaga_nova):
    #alterando todos os detalhes da vaga
    vaga_antiga.titulo = vaga_nova.titulo
    vaga_antiga.descricao = vaga_nova.descricao
    vaga_antiga.salario = vaga_nova.salario
    vaga_antiga.tipo_contratacao = vaga_nova.tipo_contratacao
    vaga_antiga.local = vaga_nova.local
    vaga_antiga.quantidade = vaga_nova.quantidade
    vaga_antiga.contato = vaga_nova.contato
    vaga_antiga.tecnologias.set(vaga_nova.tecnologias) #altera a lista de tecnologias
    #que ssa vaga se relaciona.
    vaga_antiga.save(force_update=True)


