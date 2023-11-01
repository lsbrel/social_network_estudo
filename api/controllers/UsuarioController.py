# PYTHON
import json
import hashlib
# REST_FRAMEWORK
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# REQUESTS
from api.requests import UsuarioRequest
# MODELS
from api.models import Usuario

class UsuarioController(APIView):

    def get(self, request):

        usuarios = Usuario.objects.all()
        usuarioSerial = UsuarioRequest(usuarios, many=True)
        return Response(usuarioSerial.data, status=status.HTTP_200_OK)
    
    def post(self, request):

        senhaHash = hashlib.sha256(request.data['senha'].encode(encoding='UTF-8'))
        request.data['senha'] = senhaHash.hexdigest()
        dataSerial = UsuarioRequest(data=request.data)
        
        if dataSerial.is_valid():

            dataSerial.save()
            return Response("Dados foram salvos com sucesso", status=status.HTTP_200_OK)
            
        return Response("Não foi possível salvar os dados", status=status.HTTP_400_BAD_REQUEST)
