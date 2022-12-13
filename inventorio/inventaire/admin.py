from django.contrib import admin

from inventaire.models import Conteneur


# Register your models here.


class ConteneurAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent')


admin.site.register(Conteneur, ConteneurAdmin)
