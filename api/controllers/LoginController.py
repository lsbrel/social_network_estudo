# REQUESTS
from api.requests import LoginRequest
# CONTROLLERS
from api.controllers.Controller import Controller
# MODELS
from api.models import Login

class LoginController(Controller):
    
    def post(self, request):

        # valida se o usuario não está logado 
        try:
            if self.verificarLogin(request.headers['Authorization']):
            
                return super().apiResponse(False, "Usuario já esta logado")
        except:
            return super().apiResponse(False, "Usuario não existe")
        
        # aqui validam se os campos
        validatedData = LoginRequest(data=request.data)

        # aqui validam se os dados que vem nos campos
        if validatedData.is_valid(raise_exception=True):  
            token = validatedData.save() # caso sejam validados eles são salvos em banco

            return super().apiResponse(True, f"{token}")

        return super().apiResponse(False, 'Login não foi realizado')


    def verificarLogin(self, header):
        try:
            data = Login.objects.get(token=header)
            return True
        except:
            return False