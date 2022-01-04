from django.db import models


class Pessoa(models.Model):
    nome = models.CharField(null=False, blank=False, max_length=200)
    email = models.EmailField(null=False, blank=False)
