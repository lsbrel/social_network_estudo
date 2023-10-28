from rest_framework import serializers
# import model
from api.models import LoginModel


class LoginRequest(serializers.ModelSerializer):
    class Meta:
        model = LoginModel
        fields = ['nome', 'senha']     


