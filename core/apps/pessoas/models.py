from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(null=False, blank=False)

    def __str__(self) -> str:
        return self.nome.title()
