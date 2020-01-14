from django.db import models

# Create your models here.
class ref_region(models.Model):
    rrg_id = models.AutoField(primary_key=True)
    rrg_nombre = models.CharField(max_length=100)
    rrg_ordinal = models.CharField(max_length=100) 
    
    def __str__(self):
        return "ref_region"+self.rrg_ordinal



class ref_comuna(models.Model):
    rcm_id = models.AutoField(primary_key=True)
    rcm_nombre = models.CharField(max_length=100) 
    rcm_id_regiones =models.IntegerField()
    def __str__(self):
        return "ref_comuna"+self.rcm_nombre

class mae_sala(models.Model):
    msl_id = models.AutoField(primary_key=True)
    msl_nombre = models.CharField(max_length=100) 
    msl_numero =models.IntegerField()
    msl_activa = models.BooleanField(default=True) 
    msl_descripción=models.CharField(max_length=100)
    def __str__(self):
        return "mae_sala"

class nub_arrendar(models.Model):
    nrr_id_sala =models.ForeignKey(mae_sala, on_delete=models.CASCADE)
    nrr_id_comuna =models.ForeignKey(ref_comuna, on_delete=models.CASCADE)
    nrr_id_region=models.ForeignKey(ref_region, on_delete=models.CASCADE)
    nrr_fecha =models.DateTimeField()
    def __str__(self):
        return "nub_arrendar"
