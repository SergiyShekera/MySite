from django.db import models

# Create your models here.

class Univ(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def __repr__(self):
        return f'<Univ (name={self.name})>'

