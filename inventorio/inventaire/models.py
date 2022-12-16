from django.db import models


# Create your models here.
class Categorie(models.Model):
    name = models.fields.CharField(max_length=100)
    description = models.CharField(max_length=300,
                                   null=True,
                                   blank=True)

    def __str__(self):
        return f'{self.name}'


class Conteneur(models.Model):
    name = models.fields.CharField(max_length=100)
    categorie = models.ForeignKey('Categorie',
                                  null=True,
                                  blank=True,
                                  default=None,
                                  on_delete=models.SET_DEFAULT,
                                  related_name='conteneur')
    parent = models.ForeignKey('self',
                               null=True,
                               blank=True,
                               default=None,
                               on_delete=models.SET_DEFAULT,
                               related_name='child')

    def set_parent(self, parent):
        self.parent = parent

    def get_first_child(self):
        return self.child.first()

    def get_child(self):
        return self.child.all()

    def get_child_recursively(self):
        if self.get_child():
            for child in self.get_child():
                print(child)

    def __str__(self):
        return f'{self.name}'



