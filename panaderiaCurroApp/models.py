from django.db import models

# Create your models here.
class Panaderia(models.Model):
    nombre = models.CharField(max_length=150,blank=False)
    direccion = models.CharField(max_length=250)
    anyo_fundacion = models.IntegerField(null=False)

    def __str__(self):
        return self.nombre


class Panadero(models.Model):
    nombre = models.CharField(max_length=150, blank=False)
    apellidos = models.CharField(max_length=150, blank=False)
    fecha_nacimiento = models.DateField(null=False)
    panaderia = models.ForeignKey(Panaderia,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre + "," + self.apellidos