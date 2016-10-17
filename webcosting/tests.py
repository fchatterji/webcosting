# -*- coding: utf-8 -*-

from django.test import TestCase

from webcosting.models import Projet, LanguageDeProgrammation, TailleProjet, Coefficient, Fonction, TypeFonction

from django.core.exceptions import ObjectDoesNotExist

class ProjetTestCase(TestCase):
    fixtures = ['fixture.json']
    """Fixture créée pour intégrer toutes les donnée de configuration.

    Pour recréer une fixture, utiliser la commande suivante pour éviter des
    erreurs:
    python manage.py dumpdata -o fixture.json --indent=4 -e sessions -e admin -e contenttypes -e auth.Permission --natural-primary --natural-foreign
    """

    def setUp(self):

        petit = TailleProjet.objects.get(taille_projet="petit")
        java = LanguageDeProgrammation.objects.get(language_de_programmation="Java")

        projet = Projet.objects.create(
            nom_projet="projet1",
            taille_projet=petit,
            language_de_programmation=java,
            type_projet='OR',
        )

    def test_unicode(self):
        projet = Projet.objects.get(nom_projet="projet1")
        self.assertEqual(projet.__unicode__(), projet.nom_projet)

    def test_valeurs_par_defaut(self):
        projet = Projet.objects.get(nom_projet="projet1")

        self.assertEqual(projet.nom_projet, "projet1")

        self.assertEqual(projet.fiab, 1.00)
        self.assertEqual(projet.donn, 1.00)
        self.assertEqual(projet.cplx, 1.00)
        self.assertEqual(projet.temp, 1.00)
        self.assertEqual(projet.espa, 1.00)
        self.assertEqual(projet.virt, 1.00)
        self.assertEqual(projet.csys, 1.00)
        self.assertEqual(projet.apta, 1.00)
        self.assertEqual(projet.expa, 1.00)
        self.assertEqual(projet.aptp, 1.00)
        self.assertEqual(projet.expv, 1.00)
        self.assertEqual(projet.expl, 1.00)
        self.assertEqual(projet.pmod, 1.00)
        self.assertEqual(projet.olog, 1.00)
        self.assertEqual(projet.dreq, 1.00)

        self.assertEqual(projet.point_de_fonction_brut, 0)
        self.assertEqual(projet.facteur_ajustement, 1)
        self.assertEqual(projet.point_de_fonction_net, 0)
        self.assertEqual(projet.charge_de_travail_point_de_fonction, 0)
        self.assertEqual(projet.charge_de_travail_point_de_fonction_mois, 0)
        self.assertEqual(projet.kilo_ligne_de_code, 0)

        self.assertEqual(projet.effort_simple, 0)

        self.assertEqual(projet.effort_intermediaire, 0)

        self.assertEqual(projet.temps_de_developpement, 0)
        self.assertEqual(projet.get_absolute_url(), u'/projet/1/')


class FonctionTestCase(TestCase):
    fixtures = ['fixture.json']

    def setUp(self):

        petit = TailleProjet.objects.get(taille_projet="petit")
        java = LanguageDeProgrammation.objects.get(language_de_programmation="Java")

        projet = Projet.objects.create(
            nom_projet="projet1",
            taille_projet=petit,
            language_de_programmation=java,
            type_projet='OR',
        )

        type_fonction = TypeFonction.objects.get(type_fonction='GDI')

        fonction = Fonction.objects.create(
            projet=projet,
            nom_fonction='fonction1',
            type_fonction=type_fonction,
        )

    def test_valeurs_par_defaut(self):
        fonction = Fonction.objects.get(nom_fonction='fonction1')

        self.assertEqual(fonction.__unicode__(), 'fonction1')
        self.assertEqual(fonction.nom_fonction, 'fonction1')
        self.assertEqual(fonction.nombre_sous_fonction, 0)
        self.assertEqual(fonction.nombre_donnees_elementaires, 0)
        self.assertEqual(fonction.get_absolute_url(), u'/projet/1/fonction/')
        self.assertEqual(fonction.point_de_fonction_brut, 0)
        self.assertEqual(fonction.point_de_fonction_net, 0)

    def test_point_de_fonction_brut(self):
        fonction = Fonction.objects.get(nom_fonction='fonction1')
        fonction.nombre_sous_fonction = 1
        self.assertEqual(fonction.point_de_fonction_brut, 0)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        fonction.nombre_sous_fonction = 5
        self.assertEqual(fonction.point_de_fonction_brut, 0)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        fonction.nombre_sous_fonction = 99
        self.assertEqual(fonction.point_de_fonction_brut, 0)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        fonction.nombre_sous_fonction = 0
        fonction.nombre_donnees_elementaires = 1
        self.assertEqual(fonction.point_de_fonction_brut, 7)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        fonction.nombre_sous_fonction = 0.5
        fonction.nombre_donnees_elementaires = 1.5
        self.assertEqual(fonction.point_de_fonction_brut, 7)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        fonction.nombre_sous_fonction = '10'
        fonction.nombre_donnees_elementaires = 2
        self.assertEqual(fonction.point_de_fonction_brut, 10)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        fonction.nombre_sous_fonction = '10'
        fonction.nombre_donnees_elementaires = 50
        self.assertEqual(fonction.point_de_fonction_brut, 15)
        self.assertEqual(fonction.point_de_fonction_net, fonction.point_de_fonction_brut)

        with self.assertRaises(ObjectDoesNotExist):
            fonction.nombre_sous_fonction = -5
            fonction.nombre_donnees_elementaires = -50
            fonction.point_de_fonction_brut

        with self.assertRaises(ObjectDoesNotExist):
            fonction.nombre_sous_fonction = -5
            fonction.nombre_donnees_elementaires = 10
            fonction.point_de_fonction_brut

        with self.assertRaises(ObjectDoesNotExist):
            fonction.nombre_sous_fonction = 2
            fonction.nombre_donnees_elementaires = 100000
            fonction.point_de_fonction_brut

    def test_get_absolute_url(self):
        projet = Projet.objects.get(nom_projet="projet1")
        type_fonction = TypeFonction.objects.get(type_fonction='GDI')

        fonction2 = Fonction.objects.create(
            projet=projet,
            nom_fonction='fonction2',
            type_fonction=type_fonction,
        )

        fonction3 = Fonction.objects.create(
            projet=projet,
            nom_fonction='fonction3',
            type_fonction=type_fonction,
        )

        self.assertEqual(fonction2.get_absolute_url(), u'/projet/1/fonction/')
        self.assertEqual(fonction3.get_absolute_url(), u'/projet/1/fonction/')
