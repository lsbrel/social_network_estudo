# PYTHON
import hashlib
# CONTROLLER
from api.controllers.Controller import Controller
# REQUESTS
from api.requests import UsuarioRequest
# MODELS
from api.models import Usuario

class UsuarioController(Controller):

    def get(self, request):

        usuarios = Usuario.objects.all()
        usuarioSerial = UsuarioRequest(usuarios, many=True)

        return super().apiResponse(True ,usuarioSerial.data)
    
    def post(self, request):

        senhaHash = hashlib.sha256(request.data['senha'].encode(encoding='UTF-8'))
        request.data['senha'] = senhaHash.hexdigest()
        dataSerial = UsuarioRequest(data=request.data)
        
        if dataSerial.is_valid():

            dataSerial.save()
            return super().apiResponse(True, "Dados foram salvos com sucesso")
            
        return super().apiResponse(False, "Não foi possível salvar os dados")


class UsuarioControllerId(Controller):

    def get(self,request, pk):
        
        try:
            usuario = Usuario.objects.get(pk=pk)
        except:

            return super().apiResponse(False, f'Usuario: {pk} não encontrado')

        usuarioSerial = UsuarioRequest(usuario)
        return super().apiResponse( True, usuarioSerial.data)

    def put(self, request, pk):

        try:
            usuario = Usuario.objects.get(pk=pk)
        except:
            
            return super().apiResponse(False, f'Usuario {pk} não pode ser encontrado')
            
        senhaHash = hashlib.sha256(request.data['senha'].encode(encoding='UTF-8'))
        request.data['senha'] = senhaHash.hexdigest()
        usuarioSerial = UsuarioRequest(usuario, data=request.data)

        if usuarioSerial.is_valid():
            usuarioSerial.save()

            return super().apiResponse(True, "Dados foram atualizados")

        return super().apiResponse(False, "Dados não puderam ser atualizados")
    
    def delete(self, request, pk):

        try:
            usuario = Usuario.objects.get(pk=pk)
        except:    
            return super().apiResponse(False, f'Usuario {pk} não pode ser encontrado')

        usuario.delete()
        return super().apiResponse(True, "Dado foi deletado com sucesso")    

