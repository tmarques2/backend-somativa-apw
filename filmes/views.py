from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from .models import Genero, Filme, Favorito
from .serializers import (CadastroUsuarioSerializer, GeneroSerializer, FilmeSerializer, FavoritoSerializer)
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

class CadastroUsuarioView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CadastroUsuarioSerializer
    permission_classes = [AllowAny]
    
class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer

class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer
