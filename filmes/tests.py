from io import StringIO

from django.core.management import call_command
from django.test import TestCase

from .models import Filme, Genero


class SeedCatalogTests(TestCase):
    def run_seed(self):
        call_command("seed_catalog", stdout=StringIO())

    def test_seed_creates_twelve_movies_with_genres(self):
        self.run_seed()

        self.assertEqual(Filme.objects.count(), 12)
        godfather = Filme.objects.get(titulo="O Poderoso Chefão")
        self.assertEqual(godfather.imagem, "poster_chefao.jpg")
        self.assertSetEqual(
            set(godfather.genero.values_list("nome", flat=True)),
            {"Crime", "Drama"},
        )

    def test_seed_is_idempotent(self):
        self.run_seed()
        self.run_seed()

        self.assertEqual(Filme.objects.count(), 12)

    def test_legacy_movie_is_renamed_without_changing_its_id(self):
        legacy_movie = Filme.objects.create(
            titulo="Batman Begins",
            sinopse="Registro antigo",
            ano_lancamento=2005,
            imagem="batman.jpg",
        )
        legacy_movie.genero.add(Genero.objects.create(nome="Aventura"))

        self.run_seed()

        replaced_movie = Filme.objects.get(titulo="O Poderoso Chefão")
        self.assertEqual(replaced_movie.pk, legacy_movie.pk)
        self.assertEqual(replaced_movie.imagem, "poster_chefao.jpg")
