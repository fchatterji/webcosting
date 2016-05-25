from django.contrib import admin

# Register your models here.
from .models import *

# cocomo
class CoefficientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'type_projet',
        'type_coefficient',
        'valeur_coefficient'
        )

    list_display_links = ('id',)

    list_editable = (
        'type_projet',
        'type_coefficient',
        'valeur_coefficient'
        )

admin.site.register(Coefficient, CoefficientAdmin)

# points de fonctions
class LanguageDeProgrammationAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'language_de_programmation',
        'ligne_de_code',
        )

    list_display_links = ('id',)

    list_editable = (
        'language_de_programmation',
        'ligne_de_code',
        )

admin.site.register(LanguageDeProgrammation, LanguageDeProgrammationAdmin)


admin.site.register(TailleProjet)
admin.site.register(TypeFonction)
admin.site.register(Fonction)


class CalculPointDeFonctionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type_fonction', 
        'nombre_sous_fonction_deb', 
        'nombre_sous_fonction_fin', 
        'nombre_donnees_elementaires_deb', 
        'nombre_donnees_elementaires_fin', 
        'complexite', 
        'nombre_point_de_fonction'
        )

    list_display_links = ('id',)

    list_editable = (
        'type_fonction', 
        'nombre_sous_fonction_deb', 
        'nombre_sous_fonction_fin', 
        'nombre_donnees_elementaires_deb', 
        'nombre_donnees_elementaires_fin', 
        'complexite', 
        'nombre_point_de_fonction'
        )


admin.site.register(CalculPointDeFonction, CalculPointDeFonctionAdmin)

# global
admin.site.register(Projet)
