from django import forms

from inventaire.models import Categorie, Conteneur


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = '__all__'


class ConteneurForm(forms.ModelForm):
    class Meta:
        model = Conteneur
        fields = '__all__'
