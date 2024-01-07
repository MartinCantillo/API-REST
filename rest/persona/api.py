from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persona
from .serializer import PersonaSerializer

#Esto es cuando la api es basada en clase (APIView)
#Creo la clase 
class PersonaAPIView(APIView):
    #Creo los metodos

    def get(self,request):
        #query
        personas=Persona.objects.all()
        #serializer, como personas esa quiery me va arrojar una lista , al serializer le coloco many=true
        ##personas_serializers =PersonaSerializer(personas)
        personas_serializers =PersonaSerializer(personas, Many=True)
        #retorno response , en personas_serializers.data es donde se encuentra la info en .data 
        return Response(personas_serializers.data)
