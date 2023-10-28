from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# importar requests
from api.requests import LoginRequest


class Login(APIView):
    
    def get(self, request):
        return Response(request.headers, status='200')

    def post(self, request):
        serial = LoginRequest(data=request.data)
        if serial.is_valid():
            return Response('valido', status=200)
        return Response('serial', status=404)
