from django.db import models

#Ulyses: Create models here, the apply "py manage.py makemigrations", then "py manage.py migrate"
#and changes will be updated in the database you configure in Databases in settings.py

#If model is "Person" it creates the table as "appQuart_person"

# Create your models here.

class Usuario(models.Model):
    nombre= models.CharField(max_length=80)
    apellidopaterno = models.CharField(max_length=80)
    apellidomaterno = models.CharField(max_length=80)
    empresa = models.CharField(max_length=80)
    correo = models.CharField(max_length=80)
    contrasena = models.CharField(max_length=80)
    fechacompleta =models.DateTimeField()
    autorizado = models.BooleanField()