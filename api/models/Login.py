from django.db import models

class Login(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    token = models.CharField(max_length=32)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
