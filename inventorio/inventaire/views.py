from django.shortcuts import render
from django.http import HttpResponse

from inventaire.models import Conteneur


# Create your views here.

def liste(request):
    #conteneurs = Conteneur.objects.all()
    conteneurs = Conteneur.objects.all()
    conteneurs = conteneurs[0]  # root

    print(conteneurs)
    conteneurs.get_child_recursively()

    return render(request,
                  'liste/liste.html',
                  {'conteneurs': conteneurs})
