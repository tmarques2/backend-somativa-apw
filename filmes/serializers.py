from rest_framework import serializers
from .models import Genero, Filme, Favorito
from django.contrib.auth import get_user_model

User = get_user_model()

class CadastroUsuarioSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = "__all__"

class FilmeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filme
        fields = "__all__"

class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = "__all__"