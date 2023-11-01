from django.db import models

class Usuario(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True)
    nome=models.CharField(max_length=70)
    username=models.CharField(max_length=20)
    senha=models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)
    deleted_at = models.DateField(auto_now=True)