from django.db import models
from django.conf import settings

# Create your models here.
class Genero(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Filme(models.Model):
    titulo = models.CharField(max_length=255)
    sinopse = models.TextField()
    genero = models.ManyToManyField(Genero, related_name="filmes")
    ano_lancamento = models.IntegerField()
    imagem = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo
    
class Favorito(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="favoritos")
    filme = models.ForeignKey(Filme, on_delete=models.CASCADE, related_name="favoritos")
    data_favoritado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.filme.titulo