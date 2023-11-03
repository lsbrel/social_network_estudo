# DJANGO
from django.urls import path
# CONTROLLERS
from api.controllers.LoginController import LoginController
from api.controllers.UsuarioController import UsuarioController
from api.controllers.UsuarioController import UsuarioControllerId
from api.controllers.LogoutController import LogoutController


urlpatterns = [

    # LOG IN/OUT
    path("login/", LoginController.as_view()),
    path("logout/", LogoutController.as_view()),
    # LOG IN/OUT

    # USUARIO
    path("usuario/", UsuarioController.as_view()),
    path("usuario/<int:pk>/", UsuarioControllerId.as_view())
    # USUARIO

]