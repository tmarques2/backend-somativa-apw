from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from filmes.views import GeneroViewSet, FilmeViewSet, FavoritoViewSet, CadastroUsuarioView

def home(request):
    return HttpResponse("Somativa APW")

router = DefaultRouter()
router.register(r'generos', GeneroViewSet)
router.register(r'filmes', FilmeViewSet)
router.register(r'favoritos', FavoritoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', home),
    path('api/usuarios/cadastrar/',CadastroUsuarioView.as_view(), name = 'cadastrar_usuario'),
    
    # Login - gera Access Token e Refresh Token 
    path('api/token/',
        TokenObtainPairView.as_view(),
        name= 'token_obtain_pair'
    ),
    
    # Gera um novo Access Token
    path('api/token/refresh/',
        TokenRefreshView.as_view(),
        name = 'token_refresh'
    )
]
