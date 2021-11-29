from ..models import Vaga

def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas
    #buscar as vagas dentro do banco de dados

