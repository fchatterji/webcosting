 # -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.db.models import Avg
from django.core.urlresolvers import reverse



class Coefficient(models.Model):

    def __unicode__(self):
        return self.type_projet + '-' + self.type_coefficient

    TYPE_PROJET_CHOIX = (
        ('organique', 'organique'),
        ('semi-détaché', 'semi-détaché'),
        ('embarqué', 'embarqué'),
    )

    type_projet = models.CharField(
        max_length=10, 
        choices=TYPE_PROJET_CHOIX,
        default='organique'
        )

    TYPE_COEFFICIENT_CHOIX = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    )

    type_coefficient = models.CharField(
        max_length=2, 
        choices=TYPE_COEFFICIENT_CHOIX,
        default='A',
        )

    valeur_coefficient = models.FloatField(
        default=None,
        )




class TypeAttribut(models.Model):

    def __unicode__(self):
        return self.type_attribut_detail

    type_attribut = models.CharField(
        'type de l\'attribut', 
        max_length=100, 
        default=None
        )

    type_attribut_detail = models.CharField(
        'type détaillé de l\'attribut', 
        max_length=100, 
        default=None, 
        blank=True, 
        null=True
        )




class LanguageDeProgrammation(models.Model):

    def __unicode__(self):
        return self.language_de_programmation

    language_de_programmation = models.CharField(
        'language de programmation',
        max_length=100
        )

    ligne_de_code_par_points_de_fonctions = models.IntegerField(
        'ligne de code par points de fonctions',
        )



class TailleProjet(models.Model):

    def __unicode__(self):
        return str(self.taille_projet)

    taille_projet = models.CharField(
        'taille du projet',
        max_length=30,
        )

    charge_de_travail = models.PositiveIntegerField(
        'charge de travail en jour homme par points de fonctions'
        )


class TypeFonction(models.Model):

    def __str__(self):
        return self.type_fonction

    TYPE_FONCTION_CHOIX = (
        ('GDI', 'données internes'),
        ('GDE', 'données externes'),
        ('ENT', 'entrées'),
        ('SOR', 'sorties'),
        ('INT', 'interrogation')
        )

    type_fonction = models.CharField(
        max_length=3,
        choices=TYPE_FONCTION_CHOIX,
        default='données internes'
        )


class CalculPointDeFonction(models.Model):

    type_fonction = models.ForeignKey(
        TypeFonction,
        on_delete=models.CASCADE,
        default=None
        )

    nombre_sous_fonction_deb = models.PositiveIntegerField(
        default=0
        )

    nombre_sous_fonction_fin = models.PositiveIntegerField(
        default=0
        )

    nombre_donnees_elementaires_deb = models.PositiveIntegerField(
        default=0
        )

    nombre_donnees_elementaires_fin = models.PositiveIntegerField(
        default=0
        )

    COMPLEXITE_CHOIX = (
        ('faible', 'faible'),
        ('moyen', 'moyen'),
        ('élevé', 'élevé')
        )

    complexite = models.CharField(
        max_length=10,
        choices=COMPLEXITE_CHOIX,
        default='moyen'
        )

    nombre_point_de_fonction = models.PositiveIntegerField(
        'nombre de points de fonctions',
        default=0
        )


class Projet(models.Model):

    def __unicode__(self):
        return self.nom_projet

    nom_projet = models.CharField(
        'nom du projet', 
        max_length=100,
        default=None
        )
    
    date_dernier_enregistrement = models.DateTimeField(
        'date du dernier enregistrement',
        auto_now=True,
        null=True
        ) 


    ORGANIQUE = 'OR'
    SEMIDETACHE = 'SD'
    EMBARQUE = 'EM'

    TYPE_PROJET_CHOIX = (
        (ORGANIQUE, 'organique'),
        (SEMIDETACHE, 'semi-détaché'),
        (EMBARQUE, 'embarqué'),
    )

    type_projet = models.CharField(
        max_length=2, 
        choices=TYPE_PROJET_CHOIX,
        default='organique'
        )



    taille_projet = models.ForeignKey(
        TailleProjet,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )

    language_de_programmation = models.ForeignKey(
        LanguageDeProgrammation,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        )

    facteur_ajustement = models.IntegerField(
        default=1,
        blank=True,
        null=True,
        )


    FIAB_CHOIX = (
        (0.75, 'très bas: 0.75'),
        (0.88, 'bas: 0.88'),
        (1.00, 'moyen: 1.00'),
        (1.15, 'élevé: 1.15'),
        (1.40, 'très élevé: 1.40'),
        )

    fiab = models.FloatField(
        choices=FIAB_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    DONN_CHOIX = (
        (0.94, 'bas (0.94)'),
        (1.00, 'moyen (1.00)'),
        (1.08, 'élevé (1.08)'),
        (1.16, 'très élevé (1.16)'),
        )

    donn = models.FloatField(
        choices=DONN_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    CPLX_CHOIX = (
        (0.70, 'très bas: 0.70'),
        (0.85, 'bas: 0.85'),
        (1.00, 'moyen: 1.00'),
        (1.15, 'élevé: 1.15'),
        (1.30, 'très élevé: 1.30'),
        (1.65, 'très très élevé: 1.65'),
        )

    cplx = models.FloatField(
        choices=CPLX_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    TEMP_CHOIX = (
        (1.00, 'moyen: 1.00'),
        (1.11, 'élevé: 1.11'),
        (1.30, 'très élevé: 1.30'),
        (1.66, 'très très élevé: 1.66'),
        )

    temp= models.FloatField(
        choices=TEMP_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    ESPA_CHOIX = (
        (1.00, 'moyen: 1.00'),
        (1.06, 'élevé: 1.06'),
        (1.21, 'très élevé: 1.21'),
        (1.56, 'très très élevé: 1.56'),
        )

    espa = models.FloatField(
        choices=ESPA_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    VIRT_CHOIX = (
        (0.87, 'bas: 0.87'),
        (1.00, 'moyen: 1.00'),
        (1.15, 'élevé: 1.15'),
        (1.30, 'très élevé: 1.30'),
        )

    virt = models.FloatField(
        choices=VIRT_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    CSYS_CHOIX = (
        (0.87, 'bas: 0.87'),
        (1.00, 'moyen: 1.00'),
        (1.07, 'élevé: 1.07'),
        (1.15, 'très élevé: 1.15'),
        )

    csys = models.FloatField(
        choices=CSYS_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    APTA_CHOIX = (
        (1.46, 'très bas: 1.46'),
        (1.19, 'bas: 1.19'),
        (1.00, 'moyen: 1.00'),
        (0.86, 'élevé: 0.86'),
        (0.71, 'très élevé: 0.71'),
        )

    apta = models.FloatField(
        choices=APTA_CHOIX,
        default=None,
        blank=True,
        null=True,
        )


    EXPA_CHOIX = (
        (1.29, 'très bas: 1.29'),
        (1.13, 'bas: 1.13'),
        (1.00, 'moyen: 1.00'),
        (0.91, 'élevé: 0.91'),
        (0.82, 'très élevé: 0.82'),
        )

    expa = models.FloatField(
        choices=EXPA_CHOIX,
        default=None,
        blank=True,
        null=True,
        )

    APTP_CHOIX = (
        (1.42, 'très bas: 1.42'),
        (1.17, 'bas: 1.17'),
        (1.00, 'moyen: 1.00'),
        (0.86, 'élevé: 0.86'),
        (0.70, 'très élevé: 0.70'),
        )

    aptp = models.FloatField(
        choices=APTP_CHOIX,
        default=None,
        blank=True,
        null=True,
        )



    EXPV_CHOIX = (
        (1.21, 'très bas: 1.21'),
        (1.10, 'bas: 1.10'),
        (1.00, 'moyen: 1.00'),
        (0.95, 'élevé: 0.95'),
        )

    expv = models.FloatField(
        choices=EXPV_CHOIX,
        default=None,
        blank=True,
        null=True,
        )


    EXPL_CHOIX = (
        (1.14, 'très bas: 1.14'),
        (1.07, 'bas: 1.07'),
        (1.00, 'moyen: 1.00'),
        (0.95, 'élevé: 0.95'),
        )

    expl = models.FloatField(
        choices=EXPL_CHOIX,
        default=None,
        blank=True,
        null=True,
        )


    PMOD_CHOIX = (
        (1.24, 'très bas: 1.24'),
        (1.10, 'bas: 1.10'),
        (1.00, 'moyen: 1.00'),
        (0.91, 'élevé: 0.91'),
        (0.82, 'très élevé: 0.82'),
        )

    pmod = models.FloatField(
        choices=PMOD_CHOIX,
        default=None,
        blank=True,
        null=True,
        )


    OLOG_CHOIX = (
        (1.24, 'très bas: 1.24'),
        (1.10, 'bas: 1.10'),
        (1.00, 'moyen: 1.00'),
        (0.91, 'élevé: 0.91'),
        (0.83, 'très élevé: 0.83'),
        )

    olog = models.FloatField(
        choices=OLOG_CHOIX,
        default=None,
        blank=True,
        null=True,
        )


    DREQ_CHOIX = (
        (1.23, 'très bas: 1.23'),
        (1.08, 'bas: 1.08'),
        (1.00, 'moyen: 1.00'),
        (1.04, 'élevé: 1.04'),
        (1.10, 'très élevé: 1.10'),
        )

    dreq = models.FloatField(
        choices=DREQ_CHOIX,
        default=None,
        blank=True,
        null=True,
        )


    def get_absolute_url(self):
        return reverse('webcosting:projet', kwargs={'pk':self.pk})


    def _point_de_fonction_brut(self):

        fonctions = Fonction.objects.filter(projet=self.id)
        
        point_de_fonction_brut = 0
        for fonction in fonctions:
            point_de_fonction_brut += fonction.point_de_fonction_brut

        return point_de_fonction_brut

    point_de_fonction_brut = property(_point_de_fonction_brut)


    def _point_de_fonction_net(self):

        return self.facteur_ajustement * self.point_de_fonction_brut

    point_de_fonction_net = property(_point_de_fonction_net)



    def _charge_de_travail_point_de_fonction(self):

        taille_projet = TailleProjet.objects.get(taille_projet=self.taille_projet)

        charge_de_travail = taille_projet.charge_de_travail

        return charge_de_travail * self.point_de_fonction_net

    charge_de_travail_point_de_fonction = property(_charge_de_travail_point_de_fonction)



    def _ligne_de_code(self):

        language_de_programmation = LanguageDeProgrammation.objects.get(language_de_programmation=self.language_de_programmation)

        ligne_de_code_par_points_de_fonctions = language_de_programmation.ligne_de_code_par_points_de_fonctions
        
        return ligne_de_code_par_points_de_fonctions * self.point_de_fonction_net / 1000.0

    ligne_de_code = property(_ligne_de_code)



    def _effort_simple(self):



        A = Coefficient.objects.get(
            type_coefficient='A',
            type_projet=self.type_projet,
            )

        B = Coefficient.objects.get(
            type_coefficient='B',
            type_projet=self.type_projet,
            )

        A = A.valeur_coefficient

        B = B.valeur_coefficient

        ligne_de_code = self.ligne_de_code

        effort_simple = A * (ligne_de_code ** B)

        effort_simple = round(effort_simple, 2)

        return effort_simple     

    effort_simple = property(_effort_simple)  




    def _charge_de_travail_cocomo(self):

        effort_simple = self.effort_simple

        moyenne_degres_integration = self.fiab / 1.0

        effort_intermediaire = moyenne_degres_integration * effort_simple

        effort_intermediaire = round(effort_intermediaire, 2)

        return effort_intermediaire

    charge_de_travail_cocomo = property(_charge_de_travail_cocomo)


    def _temps_de_developpement(self):

        C = Coefficient.objects.get(
            type_coefficient='C',
            type_projet=self.type_projet
            )

        D = Coefficient.objects.get(
            type_coefficient='D',
            type_projet=self.type_projet
            )

        C = C.valeur_coefficient

        D = D.valeur_coefficient

        effort_simple = self.effort_simple

        temps_de_developpement = C * (effort_simple ** D)

        temps_de_developpement = round(temps_de_developpement, 2)
        
        return temps_de_developpement

    temps_de_developpement = property(_temps_de_developpement)


class Fonction(models.Model):

    def __unicode__(self):
        return self.nom_fonction

    projet = models.ForeignKey(
        Projet,
        on_delete=models.CASCADE,
        default=None
        )

    nom_fonction = models.CharField(
        'nom de la fonction',
        max_length=100,
        default=None
        )

    type_fonction = models.ForeignKey(
        TypeFonction,
        on_delete=models.CASCADE,
        default=None
        )

    nombre_sous_fonction = models.PositiveIntegerField(
        'nombre de sous-fonctions (\'GDR ou SLD\')',
        default=0,
        )

    nombre_donnees_elementaires = models.PositiveIntegerField(
        'nombre de données élémentaires',
        default=0,
        )

    def get_absolute_url(self):
        return reverse('webcosting:fonction', kwargs={'projet_id':self.projet.id })


    def _point_de_fonction_brut(self):

        calcul_point_de_fonction = CalculPointDeFonction.objects.get(
            type_fonction=self.type_fonction,
            nombre_sous_fonction_deb__lte=self.nombre_sous_fonction,
            nombre_sous_fonction_fin__gte=self.nombre_sous_fonction,
            nombre_donnees_elementaires_deb__lte=self.nombre_donnees_elementaires,
            nombre_donnees_elementaires_fin__gte=self.nombre_donnees_elementaires 
            )
        return calcul_point_de_fonction.nombre_point_de_fonction

    point_de_fonction_brut = property(_point_de_fonction_brut)


    def _point_de_fonction_net(self):

        return self.projet.facteur_ajustement * self.point_de_fonction_brut

    point_de_fonction_net = property(_point_de_fonction_net)











