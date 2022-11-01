
from django.db import models

# Create your models here.
class Mensaje(models.Model):
    texto = models.CharField(max_length = 250)
    fecha = models.DateField(blank = True,  null=True)
    def __str__(self): #Para poder ver en texto en el admin y no  como objeto 1
        return self.texto