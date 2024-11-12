from django.db import models

# Create your models here.

class cliente(models.Model):
    id_cliente=models.PositiveSmallIntegerField(primary_key=True)
    nom_cliente=models.CharField(max_length=15)
    apelli_cliente=models.CharField(max_length=15)
    edad_cliente=models.CharField(max_length=2)
    tel_cliente=models.CharField(max_length=13)
    email_cliente=models.CharField(max_length=50)
    fech_reg=models.DateField()

    def __str__(self):
        return self.nom_cliente
