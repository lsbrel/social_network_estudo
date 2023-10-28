from django.urls import path
from api.controllers import Login


urlpatterns = [
    path("login", Login.as_view())
]