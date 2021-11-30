from django.contrib import admin
from django.urls import path, include
from .views import tecnologia_views, vagas_views, usuario_view
from .services import *


urlpatterns = [    
    path('tecnologias/', tecnologia_views.TecnologiaList.as_view(), name='tecnologia-list'),
    path('tecnologias/<int:id>', tecnologia_views.TecnologiaDetalhes.as_view(), name='tecnologia-detalhes'),
    path('vagas/', vagas_views.VagaList.as_view(), name='vaga-list'),
    path('vagas/<int:id>', vagas_views.VagaDetalhes.as_view(), name='vaga-detalhes'),
    path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario-list'),
]

