from django.db import models

class Post(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    titulo=models.CharField(max_length=30)
    conteudo=models.TextField(max_length=200)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(auto_now=True)