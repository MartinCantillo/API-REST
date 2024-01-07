from django.urls import path
#importo la clase de la api
from .api import PersonaAPIView

#Creo las rutas

urlpatterns=[
  path('persona/', PersonaAPIView.as_view(), name='personaApi')
 ]