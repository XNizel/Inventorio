from django.shortcuts import render
from django.http import HttpResponse

from inventaire.models import Conteneur
from inventaire.models import Categorie


# Create your views here.

def liste(request):
    # conteneurs = Conteneur.objects.all()
    conteneurs = Conteneur.objects.all()
    conteneurs = conteneurs[0]  # root

    #print(conteneurs)
    #conteneurs.get_child_recursively()

    return render(request,
                  'liste/liste.html',
                  {'conteneurs': conteneurs})


def conteneur_detail(request, id):
    conteneur = Conteneur.objects.get(id=id)
    print(conteneur.id)
    return render(request,
                  'liste/conteneur_detail.html',
                  {'conteneur': conteneur})


def categorie_list(request):
    categories = Categorie.objects.all()
    return render(request,
                  'categorie/categorie.html',
                  {'categories': categories})
