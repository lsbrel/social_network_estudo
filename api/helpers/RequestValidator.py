# REST_FRAMEWORK
from rest_framework import status
from rest_framework.response import Response
from rest_framework import serializers

class RequestValidator:
    # Classe de email que retorna se o email é valido
    @staticmethod
    def email(email):

        if '@' in email and '.com' in email:

            return True    
        raise serializers.ValidationError("exception")

    @staticmethod
    def size(input, size):
        
        if len(input) == size:

            return True
        raise serializers.ValidationError("exception")

    @staticmethod
    def min(input, size):
        
        if len(input) >= size:

            return True
        raise serializers.ValidationError("exception")


    @staticmethod
    def max(input, size):
        
        if len(input) <= size:

            return True
        raise serializers.ValidationError("exception")

    @staticmethod
    def validatorErrorResponse(info, campo, mensagem):
        response = {}
        response['status'] = info
        response['campo'] = campo
        response['mensagem'] = mensagem
        return Response(response, status=status.HTTP_201_CREATED)