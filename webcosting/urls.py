from django.conf.urls import url

from . import views

app_name = 'webcosting'

urlpatterns = [

    # ex: /webcosting/
    url(
        r'^$', 
        views.IndexView.as_view(), 
        name='index'
        ),

    # webcosting/projet/add
    url(
        r'^projet/add/$', 
        views.ProjetCreate.as_view(),
        name='projet_add'
        ),

    # webcosting/projet/2/update
    url(
        r'^projet/(?P<pk>[0-9]+)/update/$', 
        views.ProjetUpdate.as_view(),
        name='projet_update'
        ),

    # webcosting/projet/2/delete
    url(
        r'^projet/(?P<pk>[0-9]+)/delete/$',
        views.ProjetDelete.as_view(),
        name='projet_delete'
        ),

    # webcosting/projet/2/
    url(
        r'^projet/(?P<pk>[0-9]+)/$', 
        views.ProjetView.as_view(),
        name='projet'
        ),





    # ex: /webcosting/projet/2/degre_integration
    url(
        r'^projet/(?P<projet_id>[0-9]+)/degre_integration/$', 
        views.DegreIntegrationView.as_view(), 
        name='degre_integration'
        ),


    # webcosting/projet/2/degre_integration/add
    url(
        r'^projet/(?P<projet_id>[0-9]+)/degre_integration/add/$', 
        views.DegreIntegrationCreate.as_view(),
        name='degre_integration_add'
        ),

    # webcosting/projet/2/degre_integration/2/update
    url(
        r'^projet/(?P<projet_id>[0-9]+)/degre_integration/(?P<pk>[0-9]+)/update/$', 
        views.DegreIntegrationUpdate.as_view(),
        name='degre_integration_update'
        ),

    # webcosting/projet/2/fonction/2/delete
    url(
        r'^projet/(?P<projet_id>[0-9]+)/degre_integration/(?P<pk>[0-9]+)/delete/$',
        views.DegreIntegrationDelete.as_view(),
        name='degre_integration_delete'
        ),




    # ex: /webcosting/projet/2/fonction
    url(
        r'^projet/(?P<projet_id>[0-9]+)/fonction/$', 
        views.FonctionView.as_view(), 
        name='fonction'
        ),

    # webcosting/projet/2/fonction/add
    url(
        r'^projet/(?P<projet_id>[0-9]+)/fonction/add/$', 
        views.FonctionCreate.as_view(),
        name='fonction_add'
        ),

    # webcosting/projet/2/fonction/2/update
    url(
        r'^projet/(?P<projet_id>[0-9]+)/fonction/(?P<pk>[0-9]+)/update/$', 
        views.FonctionUpdate.as_view(),
        name='fonction_update'
        ),

    # webcosting/projet/2/fonction/2/delete
    url(
        r'^projet/(?P<projet_id>[0-9]+)/fonction/(?P<pk>[0-9]+)/delete/$',
        views.FonctionDelete.as_view(),
        name='fonction_delete'
        ),


    ]

