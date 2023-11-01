from django.db import models 

class UsuarioPost(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)