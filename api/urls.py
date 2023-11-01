# DJANGO
from django.urls import path
# CONTROLLERS
from api.controllers import UsuarioController


urlpatterns = [
    path("usuario", UsuarioController.as_view())
]