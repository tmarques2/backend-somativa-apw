from django.core.management.base import BaseCommand
from django.db import transaction

from filmes.models import Filme, Genero


MOVIES = [
    {
        "titulo": "Batman: O Cavaleiro das Trevas",
        "sinopse": "Em Gotham, um vigilante enfrenta um criminoso imprevisível que põe à prova os limites da cidade e do próprio herói.",
        "ano_lancamento": 2008,
        "imagem": "poster-batman.jpg",
        "generos": ["Ação", "Aventura", "Drama"],
    },
    {
        "titulo": "Malévola",
        "sinopse": "Após ser traída, uma guardiã de um reino mágico lança uma maldição sobre uma princesa e passa a questionar o conflito que ajudou a criar.",
        "ano_lancamento": 2014,
        "imagem": "poster_malevola.jpg",
        "generos": ["Aventura", "Família", "Fantasia"],
    },
    {
        "titulo": "The Matrix",
        "sinopse": "Um programador descobre que a realidade cotidiana esconde uma simulação e se junta a um grupo que luta para revelar a verdade.",
        "ano_lancamento": 1999,
        "imagem": "poster_matrix.svg",
        "generos": ["Ação", "Ficção científica"],
    },
    {
        "titulo": "Interestelar",
        "sinopse": "Com a Terra enfrentando uma crise ambiental, uma equipe parte em busca de um novo lar para a humanidade, atravessando distâncias e dilemas.",
        "ano_lancamento": 2014,
        "imagem": "interstelar-poster.jpg",
        "generos": ["Aventura", "Drama", "Ficção científica"],
    },
    {
        "titulo": "Coringa",
        "sinopse": "Um homem isolado, em busca de reconhecimento, mergulha em uma transformação que expõe tensões profundas na cidade.",
        "ano_lancamento": 2019,
        "imagem": "joker-poster.jpg",
        "generos": ["Crime", "Drama", "Suspense"],
    },
    {
        "titulo": "Duna",
        "sinopse": "Em um planeta desértico cobiçado por seu recurso raro, um jovem herdeiro enfrenta intrigas políticas e o destino de seu povo.",
        "ano_lancamento": 2021,
        "imagem": "poster-duna.jpg",
        "generos": ["Aventura", "Drama", "Ficção científica"],
    },
    {
        "titulo": "Vingadores: Ultimato",
        "sinopse": "Após uma perda devastadora, um grupo de heróis tenta encontrar uma forma de reverter o desastre e restaurar a esperança.",
        "ano_lancamento": 2019,
        "imagem": "poster-vingadores.jpg",
        "generos": ["Ação", "Aventura", "Ficção científica"],
    },
    {
        "titulo": "Crepúsculo",
        "sinopse": "Uma jovem se muda para uma pequena cidade e se aproxima de um colega enigmático, descobrindo segredos que alteram sua vida.",
        "ano_lancamento": 2008,
        "imagem": "crepusculo-poster.jpg",
        "generos": ["Drama", "Fantasia", "Romance"],
    },
    {
        "titulo": "A Origem",
        "sinopse": "Um especialista em invadir sonhos recebe a missão de implantar uma ideia na mente de um alvo, enfrentando camadas de realidade e lembranças.",
        "ano_lancamento": 2010,
        "imagem": "poster_origem.svg",
        "generos": ["Ação", "Ficção científica", "Suspense"],
    },
    {
        "titulo": "O Poderoso Chefão",
        "sinopse": "O patriarca de uma família mafiosa transfere gradualmente o comando de seus negócios para o filho mais novo, que tenta manter a família unida.",
        "ano_lancamento": 1972,
        "imagem": "poster_chefao.jpg",
        "generos": ["Crime", "Drama"],
    },
    {
        "titulo": "Clube da Luta",
        "sinopse": "Um funcionário insatisfeito conhece um homem carismático e, juntos, criam um clube secreto que toma proporções inesperadas.",
        "ano_lancamento": 1999,
        "imagem": "poster_clube_luta.jpg",
        "generos": ["Drama", "Suspense"],
    },
    {
        "titulo": "Forrest Gump: O Contador de Histórias",
        "sinopse": "Com uma visão singular do mundo, Forrest atravessa décadas de mudanças nos Estados Unidos enquanto acompanha sua própria jornada.",
        "ano_lancamento": 1994,
        "imagem": "ForrestGumpPoster.jpg",
        "generos": ["Drama", "Romance"],
    },
]


class Command(BaseCommand):
    help = "Adiciona filmes e gêneros de exemplo ao catálogo."

    @transaction.atomic
    def handle(self, *args, **options):
        Filme.objects.filter(titulo="Batman Begins").update(titulo="O Poderoso Chefão")
        created_count = 0

        for movie_data in MOVIES:
            data = movie_data.copy()
            genre_names = data.pop("generos")
            movie, created = Filme.objects.update_or_create(
                titulo=data["titulo"],
                defaults=data,
            )
            movie.genero.set(
                Genero.objects.get_or_create(nome=name)[0]
                for name in genre_names
            )
            created_count += int(created)

        self.stdout.write(
            self.style.SUCCESS(
                f"Catálogo pronto: {len(MOVIES)} filmes; "
                f"{created_count} novos nesta execução."
            )
        )
