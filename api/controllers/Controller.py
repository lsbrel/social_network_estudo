# REST_FRAMEWORK
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class Controller(APIView):

    def validationRequet():
        
        return True

    def apiResponse(self, value, content):
        response = {}
        response['status'] = value
        response['content'] = content

        return Response(response, status=status.HTTP_201_CREATED)