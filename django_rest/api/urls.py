from django.contrib import admin
from django.urls import path, include
from .views import tecnologia_views 

urlpatterns = [    
    path('tecnologias/', tecnologia_views.TecnologiaList.as_view(), name='tecnologia-list'),
]

