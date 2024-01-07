from django.urls import path
#importo la clase de la api
#from .api import PersonaAPIView
#cuando es por funcion 
from .api import Persona_api_view,Persona_detail_api_view

#Creo las rutas

#cuando es mediante clase 
'''
urlpatterns=[
  path('persona/', PersonaAPIView.as_view(), name='personaApi')
 ]
 '''

#Cuando es mediante funcion
urlpatterns=[
  path('persona/', Persona_api_view, name='personaApi'),
  path('persona_d/<int:pk>/',Persona_detail_api_view,name='persona_d')#<int:pk> para pasarle datos
 ]