# Controllers
from api.controllers.Controller import Controller
# Requests
from api.requests.PostRequest import CriarPostRequest
# Models
from api.models import UsuarioPost
from api.models import Post


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

            return super().apiResponse(True, "Post criado")

        return super().apiResponse(True, "Post não pode ser criado")
    

class PostControllerId(Controller):
    
    def get(self, request, pk):

        return super().apiResponse(True, f"{pk}")