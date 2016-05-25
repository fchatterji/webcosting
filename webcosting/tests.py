from django.test import TestCase

from .models import *


class ProjetTests(TestCase):

    taille_du_projet = TailleDuProjet(
        taille_du_projet="petit",
        )

    language_de_programmation = LanguageDeProgrammation(
        language_de_programmation="java"
        )

    projet = Projet(
        nom_projet="test",
        taille_du_projet=taille_du_projet,
        language_de_programmation=language_de_programmation,
        )

    def test_Projet(self):
        self.assertEqual(self.projet.nom_projet, "test")

    def test_point_de_fonction_brut(self):
        pass
