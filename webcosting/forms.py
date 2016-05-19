from django import forms

from .models import Projet, Fonction
from django.forms import ModelForm, modelformset_factory, BaseModelFormSet


class BaseFonctionFormSet(BaseModelFormSet):
    def __init__(self, *args, **kwargs):
        super(BaseFonctionFormSet, self).__init__(*args, **kwargs)
        self.queryset = Fonction.objects.filter(fonction__projet__id=self.kwargs['projet_id'])


 

FonctionFormSet = modelformset_factory(
    Fonction, 
    fields=('nom_fonction', 'type_fonction', 'nombre_sous_fonction', 'nombre_donnees_elementaires'), 
    )



class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = ['nom_projet']