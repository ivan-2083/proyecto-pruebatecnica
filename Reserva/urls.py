from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import permission_required
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from . import views
from rest_framework import routers



urlpatterns = [
    path('', views.index, name='index'),
    path('Arrendar',views.ArrendarSala,name="ArrendarSala"),



  


]