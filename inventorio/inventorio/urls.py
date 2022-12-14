"""inventorio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventaire import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('liste/', views.liste, name='liste-tree'),
    path('liste/<int:id>/', views.conteneur_detail, name='conteneur-detail'),
    path('liste/add', views.conteneur_add, name='conteneur-add'),
    path('liste/<int:id>/update', views.conteneur_update, name='conteneur-update'),
    path('liste/<int:id>/delete', views.conteneur_delete, name='conteneur-delete'),

    path('categorie/', views.categorie_list, name='categorie-list'),
    path('categorie/<int:id>', views.categorie_detail, name='categorie-detail'),
    path('categorie/add/', views.categorie_add, name='categorie-add'),
    path('categorie/<int:id>/update', views.categorie_update, name='categorie-update'),
    path('categorie/<int:id>/delete', views.categorie_delete, name='categorie-delete')

]
