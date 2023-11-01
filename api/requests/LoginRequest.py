from rest_framework import serializers
# import model
from api.models import Login


class LoginRequest(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = ['nome', 'senha']     


