from django.contrib import admin
from .models import Genero, Filme, Favorito

# Register your models here.
admin.site.register(Genero)
admin.site.register(Filme)
admin.site.register(Favorito)

#super usuario: senai
#senha: senai123