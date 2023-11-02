#PYTHON
import secrets
import hashlib
# REST_FRAMEWORK
from rest_framework import serializers
# MODELS
from api.models import Usuario
from api.models import Login

class LoginRequest(serializers.Serializer):

    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    senha = serializers.CharField()

    def validate(self, data):

        try:
            senhaHash = hashlib.sha256(data['senha'].encode(encoding='UTF-8'))
            data['senha'] = senhaHash.hexdigest()
            model = Usuario.objects.get(username=data['username'], senha=data['senha'])
            self.id = model.id
        except:
            raise serializers.ValidationError("Usuario não existe")

        return data
    
    def save(self):
        model = Login(
            usuario_id=self.id,
            token=secrets.token_hex(16)
        )
        model.save()

    def getId(self):
        id = Usuario.objects.get(username=self.data['username'])
        raise serializers.ValidationError("id")
