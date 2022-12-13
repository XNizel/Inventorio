from django.db import models


# Create your models here.

class Conteneur(models.Model):
    name = models.fields.CharField(max_length=100)
    parent = models.ForeignKey('self',
                               default=1,
                               on_delete=models.SET_DEFAULT)

    def __str__(self):
        return f'{self.name}'
