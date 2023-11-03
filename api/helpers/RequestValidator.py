# REST_FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

class RequestValidator:
    # Classe de email que retorna se o email é valido
    @staticmethod
    def email(email):

        if '@' in email and '.com' in email:

            return True    
        return RequestValidator.validatorErrorResponse("email", "Tipo de email não é valido")

    @staticmethod
    def size(input, size):
        
        if len(input) == size:

            return True
        return RequestValidator.validatorErrorResponse("size", f"Campo precisa ter {size} caracteres")

    @staticmethod
    def min(input, size):
        
        if len(input) >= size:

            return True
        return RequestValidator.validatorErrorResponse("min", f'Campo precisa ter no minimo {size} de catacteres')


    @staticmethod
    def max(input, size):
        
        if len(input) <= size:

            return True
        return RequestValidator.validatorErrorResponse("max", f'Campo precisa ter no maximo {size} de caracteres')

    @staticmethod
    def validatorErrorResponse(campo, mensagem):
        return Response(f'{campo}: {mensagem}', status=status.HTTP_201_CREATED)