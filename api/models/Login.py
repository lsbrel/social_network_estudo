from django.db import models

class Login(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    nome = models.CharField(max_length=120)
    senha = models.BooleanField(default=False)
    token = models.CharField(max_length=16)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
