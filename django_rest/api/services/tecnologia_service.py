from django.http.response import Http404
from ..models import Tecnologia

def listar_tecnologias(): #metodo que vai obter todas as tecnologias do banco
    #de dados e retornar a lista de tecnologias
    tecnologias = Tecnologia.objects.all()
    return tecnologias


def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome=tecnologia.nome)


def listar_tecnologia_id(id):
    try:
        return Tecnologia.objects.get(id=id) #busca no banco de dados pelas
    #id que estamos enviando como parametro
    except Tecnologia.DoesNotExist:
        raise Http404

def editar_tecnologia(tecnologia_antiga, tecnologia_nova):
    tecnologia_antiga.nome = tecnologia_nova.nome
    tecnologia_antiga.save(force_update=True) #forcando o update dessa tecnologia
    

