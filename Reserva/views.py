from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import nub_arrendar,ref_comuna,ref_region,mae_sala
from rest_framework import viewsets
from .serializers import Arrendarserialaizer

     
     
def index(request):
    return render(request,'index.html')
 
     
     

def ArrendarSala (request):
    
    nrr_id_sala = request.POST.get('correo','')
    nrr_id_comuna = request.POST.get('nombre','')
    nrr_id_region = request.POST.get('run','')
    nrr_fecha = request.POST.get('claveUsu','')
    nrr_hora = request.POST.get('fechaNac','')
    arrendar = nub_arrendar(nrr_id_sala=nrr_id_sala,nrr_id_comuna=nrr_id_comuna,nrr_id_region=nrr_id_region,nrr_fecha=nrr_fecha,nrr_hora=nrr_hora)
    arrendar.save()
      
