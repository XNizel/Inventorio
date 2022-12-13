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

    path('categorie/', views.categorie_list, name='categorie-list'),
    path('categorie/add/', views.categorie_add, name='categorie-add')

]
