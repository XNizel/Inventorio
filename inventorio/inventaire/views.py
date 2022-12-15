from django.shortcuts import render, redirect
from django.http import HttpResponse

from inventaire.models import Conteneur
from inventaire.models import Categorie

from inventaire.forms import CategorieForm


# Create your views here.

def liste(request):
    conteneurs = Conteneur.objects.all()
    conteneurs = conteneurs[0]  # root
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


def categorie_detail(request, id):
    categorie = Categorie.objects.get(id=id)
    return render(request,
                  'categorie/categorie_detail.html',
                  {'categorie': categorie})


def categorie_add(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            categorie = form.save()
            return redirect('categorie-detail', categorie.id)
    else:
        form = CategorieForm()

    return render(request,
                  'categorie/categorie_add.html',
                  {'form': form})


def categorie_update(request, id):
    categorie = Categorie.objects.get(id=id)
    form = CategorieForm(instance=categorie)
    return render(request,
                  'categorie/categorie_update.html',
                  {'form': form})
