# Rest framework
from rest_framework import serializers
# Models
from api.models import Post


class CriarPostRequest(serializers.Serializer):

    titulo = serializers.CharField()
    conteudo = serializers.CharField()

    def validate(self, data):
        return data


    def save(self):
        
        post = Post(
            titulo = self.data['titulo'],
            conteudo = self.data['conteudo']
        )
        post.save()

        return post

    