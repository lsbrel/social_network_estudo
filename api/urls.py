# DJANGO
from django.urls import path
# CONTROLLERS
from api.controllers.LoginController import LoginController
from api.controllers.UsuarioController import UsuarioController
from api.controllers.UsuarioController import UsuarioControllerId


urlpatterns = [
    path("login/", LoginController.as_view()),
    path("usuario/", UsuarioController.as_view()),
    path("usuario/<int:pk>/", UsuarioControllerId.as_view())
]