from ..models import Tecnologia

def listar_tecnologias(): #metodo que vai obter todas as tecnologias do banco
    #de dados e retornar a lista de tecnologias
    tecnologias = Tecnologia.objects.all()
    return tecnologias

def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome=tecnologia.nome)

