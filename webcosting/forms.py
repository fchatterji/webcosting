from django.forms import ModelForm, RadioSelect
from models import Projet, Fonction


class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = ['nom_projet', 'taille_projet', 'language_de_programmation']
        widgets = {
            'taille_projet': RadioSelect,
            'language_de_programmation': RadioSelect,
        }


class FonctionForm(ModelForm):
    class Meta:
        model = Fonction
        fields = [
            'nom_fonction',
            'type_fonction',
            'nombre_sous_fonction',
            'nombre_donnees_elementaires'
        ]
        widgets = {
            'type_fonction': RadioSelect,
        }


class CocomoForm(ModelForm):
    class Meta:
        model = Projet
        fields = [
            'type_projet', 
            'fiab', 
            'donn', 
            'cplx', 
            'temp', 
            'espa', 
            'virt', 
            'csys', 
            'apta', 
            'expa', 
            'aptp', 
            'expv', 
            'expl', 
            'pmod', 
            'olog', 
            'dreq'
        ]

        widgets = {
            'type_projet': RadioSelect,
            'fiab': RadioSelect,
            'donn': RadioSelect,
            'cplx': RadioSelect,
            'temp': RadioSelect,
            'espa': RadioSelect,
            'virt': RadioSelect,
            'csys': RadioSelect,
            'apta': RadioSelect,
            'expa': RadioSelect,
            'aptp': RadioSelect,
            'expv': RadioSelect,
            'expl': RadioSelect,
            'pmod': RadioSelect,
            'olog': RadioSelect,
            'dreq': RadioSelect,
        }