from django.db import models

# Create your models here.


class Inscricao(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    createdAt = models.DateTimeField(auto_now_add=True)
    