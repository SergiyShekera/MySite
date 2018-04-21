from django.db import models

# Create your models here.

from groups.models import Group
from univ.models import Univ

class Attestat(models.Model):
    predmet = models.CharField(max_length=255)
    mark = models.IntegerField()
    date = models.DateField()

    def __repr__(self):
        return f'<Attestat' \
               f'(predmet={self.predmet},' \
               f'mark={self.mark}, ' \
               f'date={self.date}' \
               f')>'

class Students(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=False)
    univ = models.ForeignKey(Univ, on_delete=models.CASCADE, null=False, blank=False)
    attestat = models.ForeignKey(Attestat, on_delete=models.CASCADE, null=True, blank=True)

    def __repr__(self):
        return f'<Group' \
               f'(name={self.name},' \
               f'surname={self.surname},' \
               f'group={self.group},' \
               f'univ={self.univ},' \
               f'attestat={self.attestat}' \
               f')>'

