from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Receita(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicar = models.BooleanField(default=False)
    foto_receita = models.ImageField(upload_to='./fotos/%d/%m/%Y/', blank=True)

    pessoa = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nome_receita.title()
