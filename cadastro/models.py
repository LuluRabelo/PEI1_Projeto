from django.db import models

from django.db import models

class Curriculo(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    formacao = models.TextField()
    experiencia = models.TextField()
    certificados = models.TextField(blank=True)
    habilidades = models.TextField()
    idiomas = models.TextField()

    def __str__(self):
        return self.nome
