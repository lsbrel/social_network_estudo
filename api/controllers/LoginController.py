from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# importar requests
from api.requests import LoginRequest
# importar models
from api.models import Login

class Login(APIView):
    
    def get(self, request):
        data = Login.objects.all()
        return Response(data, status='200')

    def post(self, request):
        dadosSerial = LoginRequest(data=request.data)
        if dadosSerial.is_valid():  
            dadosSerial.save()
            return Response('Salvo', status=200)
        return Response('Não foi possível salvar', status=404)
