from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Projet, Fonction

from django.core.urlresolvers import reverse_lazy


class IndexView(generic.ListView):
    template_name = 'webcosting/index.html'
    context_object_name = 'all_projets'

    def get_queryset(self):
        return Projet.objects.all()


class NoProjetDefault(generic.TemplateView):
    template_name = 'webcosting/default.html'


class ProjetView(generic.DetailView):
    model = Projet
    context_object_name = 'projet'
    template_name = 'webcosting/projet.html'


class ProjetCreate(CreateView):
    model = Projet
    fields = ['nom_projet', 'taille_projet', 'language_de_programmation']


class ProjetUpdate(UpdateView):
    model = Projet
    fields = ['nom_projet', 'taille_projet', 'language_de_programmation']


class ProjetDelete(DeleteView):
    model = Projet
    success_url = reverse_lazy('webcosting:index')


class CocomoCreate(CreateView):
    model = Projet
    fields = ['type_projet', 'fiab', 'donn', 'cplx', 'temp', 'espa', 'virt', 'csys', 'apta', 'expa', 'aptp', 'expv', 'expl', 'pmod', 'olog', 'dreq']
    template_name = 'webcosting/cocomo_form.html'


class CocomoUpdate(UpdateView):
    model = Projet
    fields = ['type_projet', 'fiab', 'donn', 'cplx', 'temp', 'espa', 'virt', 'csys', 'apta', 'expa', 'aptp', 'expv', 'expl', 'pmod', 'olog', 'dreq']
    template_name = 'webcosting/cocomo_form.html'


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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FonctionCreate, self).get_context_data(**kwargs)
        # Add in the project
        self.projet = get_object_or_404(Projet, pk=self.kwargs['projet_id'])
        context['projet'] = self.projet
        return context


class FonctionUpdate(UpdateView):
    model = Fonction
    fields = [
        'nom_fonction',
        'type_fonction',
        'nombre_sous_fonction',
        'nombre_donnees_elementaires'
    ]

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FonctionUpdate, self).get_context_data(**kwargs)
        # Add in the project
        self.projet = get_object_or_404(Projet, pk=self.kwargs['projet_id'])
        context['projet'] = self.projet
        return context


class FonctionDelete(DeleteView):
    model = Fonction

    def get_success_url(self):
        if 'projet_id' in self.kwargs:
            projet_id = self.kwargs['projet_id']

        return reverse('webcosting:fonction', kwargs={'projet_id': projet_id})
