#definindo o serializer do cadastro de usuarios
#usaremos a tabela default do Django
from rest_framework import serializers
from django.contrib.auth.models import User
#model padrao de autentaticao do Django

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    
    #sobrescrevendo o metodo create
    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
            #cripografando a senha com o metodo set_password
        user.save()
        return user