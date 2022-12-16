from django.shortcuts import render, redirect
from django.http import HttpResponse

from inventaire.models import Conteneur
from inventaire.models import Categorie

from inventaire.forms import CategorieForm, ConteneurForm


# Create your views here.

def liste(request):
    conteneurs = Conteneur.objects.all()
    conteneur = conteneurs[0]  # root
    return render(request,
                  'liste/liste.html',
                  {'conteneur': conteneur})


def conteneur_detail(request, id):
    conteneur = Conteneur.objects.get(id=id)
    return render(request,
                  'liste/conteneur_detail.html',
                  {'conteneur': conteneur})


def conteneur_add(request):
    if request.method == 'POST':
        form = ConteneurForm(request.POST)
        if form.is_valid():
            conteneur = form.save()
            return redirect('conteneur-detail', conteneur.id)
    else:
        form = ConteneurForm()

    return render(request,
                  'liste/conteneur_add.html',
                  {'form': form})


def conteneur_update(request, id):
    conteneur = Conteneur.objects.get(id=id)

    if request.method == 'POST':
        form = ConteneurForm(request.POST, instance=conteneur)
        if form.is_valid():
            form.save()
            return redirect('conteneur-detail', conteneur.id)

    else:
        form = ConteneurForm(instance=conteneur)

    return render(request,
                  'liste/conteneur_update.html',
                  {'conteneur': conteneur, 'form': form})


def conteneur_delete(request, id):
    conteneur = Conteneur.objects.get(id=id)

    if request.method == 'POST':
        conteneur.delete()
        return redirect('liste-tree')

    return render(request,
                  'liste/conteneur_delete.html',
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
    args = {'cat': categorie, 'form': form}
    return render(request,
                  'categorie/categorie_update.html',
                  {'categorie': categorie, 'form': form})


def categorie_delete(request, id):
    categorie = Categorie.objects.get(id=id)

    if request.method == 'POST':
        categorie.delete()
        return redirect('categorie-list')

    return render(request,
                  'categorie/categorie_delete.html',
                  {'categorie': categorie})
