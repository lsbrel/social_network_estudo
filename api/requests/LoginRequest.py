# REST_FRAMEWORK
from rest_framework import serializers
# MODELS
from api.models import Usuario
from api.models import Login
# HELPERS
from api.helpers import RequestValidator
from api.helpers import SenhaHash
from api.helpers import Token

class LoginRequest(serializers.Serializer):
    # Campos que a api recebe no request
    id = serializers.IntegerField(required=False)
    username = serializers.CharField()
    senha = serializers.CharField()

    def validate(self, data):

        try:
            data['senha'] = SenhaHash.hash(data['senha'])
            model = Usuario.objects.get(username=data['username'], senha=data['senha'])
            self.id = model.id
        except:
            raise serializers.ValidationError("Usuario não existe")

        return data
    
    def save(self):
        token = Token.generateToken()
        model = Login(
            usuario_id=self.id,
            token=token
        )

        model.save()
        return token

