from django.db import models

# Create your models here.

class ref_regiones(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ordinal = models.CharField(max_length=100) 
    
    def __str__(self):
        return "ref_regiones"+self.nombre



class ref_comunas(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    ordinal = models.CharField(max_length=100) 
    id_ref_regiones =models.ForeignKey(ref_regiones, on_delete=models.CASCADE, related_name='Id_regiones')
    def __str__(self):
        return "ref_comunas"+self.nombre
  
