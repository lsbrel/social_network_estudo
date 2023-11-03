# Rest framework
from rest_framework import serializers
from rest_framework.response import Response
# helpers
from api.helpers import RequestValidator
# Models
from api.models import Post


class CriarPostRequest(serializers.Serializer):

    titulo = serializers.CharField()
    conteudo = serializers.CharField()

    def validate(self, data):
        # validar requests
        RequestValidator.max(data['titulo'], 30)

        return data


    def save(self):

        post = Post(
            titulo = self.data['titulo'],
            conteudo = self.data['conteudo']
        )
        post.save()

        return post

class VisualizarPostRequest(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['titulo', 'conteudo', 'created_at']