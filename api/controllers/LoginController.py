# REQUESTS
from api.requests import LoginRequest
# CONTROLLERS
from api.controllers.Controller import Controller
# MODELS
from api.models import Login

class LoginController(Controller):
    
    def post(self, request):
        # Aqui valida o campo
        validatedData = LoginRequest(data=request.data)
        # Aqui valida os dados
        
        # dadosSerial = LoginRequest(data=request.data)

        if validatedData.is_valid(raise_exception=True):  
            validatedData.save()

            return super().apiResponse(True, "Login realizado")
        return super().apiResponse(False, 'Login não foi realizado')
