from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Projet, Fonction, DegreIntegration

from django.core.urlresolvers import reverse_lazy




class IndexView(generic.ListView):
    template_name = 'webcosting/index.html'
    context_object_name = 'all_projets'

    def get_queryset(self):
        return Projet.objects.all()


class ProjetView(generic.DetailView):
    model = Projet
    context_object_name = 'projet'
    template_name = 'webcosting/projet.html'


class ProjetCreate(CreateView):
    model = Projet
    fields = ['nom_projet', 'type_projet', 'taille_du_projet', 'language_de_programmation']


class ProjetUpdate(UpdateView):
    model = Projet
    fields = ['nom_projet', 'type_projet', 'taille_du_projet', 'language_de_programmation']


class ProjetDelete(DeleteView):
    model = Projet
    success_url = reverse_lazy('webcosting:index')







class DegreIntegrationView(generic.ListView):
    model = DegreIntegration
    template_name = 'webcosting/degreintegration.html'
    context_object_name = 'all_degres_integrations'

    def get_queryset(self):
        self.projet = get_object_or_404(Projet, pk=self.kwargs['projet_id'])
        return DegreIntegration.objects.filter(projet=self.projet)


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DegreIntegrationView, self).get_context_data(**kwargs)
        # Add in the project
        context['projet'] = self.projet
        return context


class DegreIntegrationCreate(CreateView):
    model = DegreIntegration
    fields = [
        'fiab', 
    ]

    def form_valid(self, form):
        form.instance.projet_id = self.kwargs.get('projet_id')
        return super(DegreIntegrationCreate, self).form_valid(form)




class DegreIntegrationUpdate(UpdateView):
    model = DegreIntegration
    fields = [
        'fiab'
    ]


class DegreIntegrationDelete(DeleteView):
    model = DegreIntegration
    
    def get_success_url(self):
        if 'projet_id' in self.kwargs:
            projet_id = self.kwargs['projet_id']

        return reverse('webcosting:degre_integration', kwargs={'projet_id':projet_id})











class FonctionView(generic.ListView):
    model = Fonction
    template_name = 'webcosting/fonction.html'
    context_object_name = 'all_fonctions'

    def get_queryset(self):
        self.projet = get_object_or_404(Projet, pk=self.kwargs['projet_id'])
        return Fonction.objects.filter(projet=self.projet)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FonctionView, self).get_context_data(**kwargs)
        # Add in the project
        context['projet'] = self.projet
        return context


class FonctionCreate(CreateView):
    model = Fonction
    fields = [
        'nom_fonction', 
        'type_fonction',
        'nombre_sous_fonction',
        'nombre_donnees_elementaires'
    ]

    def form_valid(self, form):
        form.instance.projet_id = self.kwargs.get('projet_id')
        return super(FonctionCreate, self).form_valid(form)




class FonctionUpdate(UpdateView):
    model = Fonction
    fields = [
        'nom_fonction', 
        'type_fonction',
        'nombre_sous_fonction',
        'nombre_donnees_elementaires'
    ]


class FonctionDelete(DeleteView):
    model = Fonction
    
    def get_success_url(self):
        if 'projet_id' in self.kwargs:
            projet_id = self.kwargs['projet_id']

        return reverse('webcosting:fonction', kwargs={'projet_id':projet_id})
        