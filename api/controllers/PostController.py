# python
import json
# Controllers
from api.controllers.Controller import Controller
# Requests
from api.requests.PostRequest import CriarPostRequest
from api.requests.PostRequest import VisualizarPostRequest
# Models
from api.models import UsuarioPost
from api.models import Post
from api.models import Login


class PostController(Controller):

    def post(self, request):
        postSerial = CriarPostRequest(data=request.data)

        if postSerial.is_valid():
            post = postSerial.save()
            # salvando a relacao
            modelRelacao = UsuarioPost(
                usuario_id = super().LoginId(request.headers['Authorization']),
                post_id = post.id
            )
            modelRelacao.save()

            return super().apiResponse(True, f"Post criado")

        return super().apiResponse(False, "Post não pode ser criado")
    

class PostControllerId(Controller):
    
    def get(self, request, pk):

        try:
            post = Post.objects.get(pk=pk)
        except:
            return super().apiResponse(False, "Post não existe")

        postSerial = CriarPostRequest(post)

        return super().apiResponse(True, postSerial.data)