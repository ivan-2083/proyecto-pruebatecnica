from __future__ import print_function
from datetime import datetime, date, time, timedelta
import calendar
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import nub_arrendar,ref_comuna,ref_region,mae_sala
from rest_framework import viewsets
from .serializers import Arrendarserialaizer,Regionserialaizer





     
def index(request):
    return render(request,'index.html',{'Region':ref_region.objects.all(),'Comuna':ref_comuna.objects.all(),'Sala':mae_sala.objects.all()})
    # selected_region = None
    # comunas = ref_comuna.objects.all()
    # regiones = ref_region.objects.all()

    # if request.method == "POST":
    #     selected_region = request.POST.get("region")
    #     regiones = regiones.filter(rrg_nombre=selected_region)
    #     comunas = comuna.filter(rcm_id_regiones=regiones.rrg_id)
 
    # comunas2 = ref_comuna.objects.order_by('region').values_list('region', flat=True)

    # context = {
    #     'regions': regions,
    #     'restaurants': restaurants,
    #     'selected_region': selected_region
    # }

    # return render(request, 'index.html', context)



def Grilla(request): 
    return render(request,'grilla.html',{'Arrendar':nub_arrendar.objects.filter(nrr_fecha__lte='2020-01-16')})
     

def ArrendarSala (request):
    
    nrr_nombre_sala = request.POST.get('sala','')
    nrr_nombre_comuna = request.POST.get('comuna','')
    nrr_nombre_region = request.POST.get('region','')
    nrr_fecha = request.POST.get('fecha','')
    nrr_hora = request.POST.get('hora','')
    arrendar = nub_arrendar(nrr_nombre_sala=nrr_nombre_sala,nrr_nombre_comuna=nrr_nombre_comuna,nrr_nombre_region=nrr_nombre_region,nrr_fecha=nrr_fecha,nrr_hora=nrr_hora)
    arrendar.save()

    # service = get_calendar_service()
    # # d = datetime.now().date()
    # # tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(days=1)
    # start = nrr_fecha
    # end = nrr_fecha


   
    # event_result = service.events().insert(calendarId='primary',
    # body={
    #     "summary": 'Automating calendar',
    #     "description": 'This is a tutorial example of automating google calendar with python',
    #     "start": {"dateTime": start},
    #     "end": {"dateTime": end},
    #     }
    #     ).execute()



    return redirect('index')   
      


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.events.readonly']

def get_calendar_service():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'Reserva/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service



