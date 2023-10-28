from django.db import models

class LoginModel(models.Model):
    nome = models.CharField(max_length=120)
    senha = models.BooleanField(default=False)
