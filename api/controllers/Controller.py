# REST_FRAMEWORK
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
# MODELS
from api.models import Login



class Controller(APIView):

    def LoginId(self, header):
        login = Login.objects.get(token=header)
        return login.usuario_id

    def apiResponse(self, value, content):
        response = {}
        response['status'] = value
        response['content'] = content

        return Response(response, status=status.HTTP_201_CREATED)