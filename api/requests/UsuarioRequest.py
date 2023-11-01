# REST_FRAMEWORK
from rest_framework import serializers
# MODELS
from api.models import Usuario

class UsuarioRequest(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['nome', 'username', 'senha']