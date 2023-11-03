# REST_FRAMEWORK
from api.controllers.Controller import Controller
# MODELS
from api.models import Login

class LogoutController(Controller):

    def post(self, request):
        try:
            login = Login.objects.get(token=request.headers['Authorization'])
        except:
            return super().apiResponse(False, "Usuario não está logado e não pode ser deslogados")

        login.delete()

        return super().apiResponse(True, "Usuario foi deslogado")

