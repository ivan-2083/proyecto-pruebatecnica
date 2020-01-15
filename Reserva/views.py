from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import nub_arrendar,ref_comuna,ref_region,mae_sala
from rest_framework import viewsets
from .serializers import Arrendarserialaizer,Regionserialaizer

     
     
def index(request):
    return render(request,'index.html',{'Region':ref_region.objects.all(),'Comuna':ref_comuna.objects.all(),'Sala':mae_sala.objects.all()})
 
     
     

def ArrendarSala (request):
    
    nrr_id_sala = request.POST.get('sala',int)
    nrr_id_comuna = request.POST.get('comuna','')
    nrr_id_region = request.POST.get('region','')
    nrr_fecha = request.POST.get('fecha','')
    nrr_hora = request.POST.get('hora','')
    arrendar = nub_arrendar(nrr_id_sala=nrr_id_sala,nrr_id_comuna=nrr_id_comuna,nrr_id_region=nrr_id_region,nrr_fecha=nrr_fecha,nrr_hora=nrr_hora)
    arrendar.save()
    return redirect('index')   
      
