from django.shortcuts import render
from django.http import HttpResponse

from inventaire.models import Conteneur


# Create your views here.

def liste(request):
    conteneurs = Conteneur.objects.all()
    return render(request,
                  'liste/liste.html',
                  {'conteneurs': conteneurs})
