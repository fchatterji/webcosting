from django import forms

from .models import Projet, DegreIntegration, Fonction
from django.forms import ModelForm, formset_factory, BaseFormSet


class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = [
            'nom_projet'
            ]


class ProjetFormCocomo(ModelForm):
    class Meta:
        model = Projet
        fields = [
            'nom_projet',
            'type_projet'
            ]
 
class DegreIntegrationForm(ModelForm):
    class Meta:
        model = DegreIntegration
        fields = [
            'type_attribut',
            'degre_integration',
            'coefficient_integration',
            ]
        
             
    fiab = forms.ModelChoiceField(
        queryset=(DegreIntegration.objects.filter(type_attribut__type_attribut="FIAB"))
        )

    donn = forms.ModelChoiceField(
        queryset=(DegreIntegration.objects.filter(type_attribut__type_attribut="DONN"))
        )


class ProjetFormPointDeFonction(ModelForm):
    class Meta:
        model = Projet
        fields = [
            'nom_projet',
            'taille_du_projet',
            'language_de_programmation'
            ]


class FonctionForm(ModelForm):
    class Meta:
        model = Fonction
        fields = [
            'projet',
            'nom_fonction',
            'type_fonction',
            'nombre_sous_fonction',
            'nombre_donnees_elementaires'
            ]

    
    point_de_fonction_brut = Fonction.point_de_fonction_brut


