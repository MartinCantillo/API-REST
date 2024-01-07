#este es para hacerlo por medio de clase
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persona
from .serializer import PersonaSerializer
#Este es para hacerlo mediante funciones
from rest_framework.decorators import api_view

#Esto es cuando la api es basada en clase (APIView)
#Basada en clase 
'''
class PersonaAPIView(APIView):
    #Creo los metodos

    def get(self,request):
        #query
        personas=Persona.objects.all()
        #serializer, como personas esa quiery me va arrojar una lista , al serializer le coloco many=true
        ##personas_serializers =PersonaSerializer(personas)
        personas_serializers =PersonaSerializer(personas, many=True)
        #retorno response , en personas_serializers.data es donde se encuentra la info en .data 
        return Response(personas_serializers.data)
'''

#Basada en funciones
@api_view(['GET','POST'])
def Persona_api_view(request):
    if request.method =='GET':
        personas = Persona.objects.all()
        personas_serializers=PersonaSerializer(personas, many=True)
        return  Response(personas_serializers.data)
    elif request.method=='POST':
        #se descerializan los datos que vienen del request
        data=request.data#datos que vienen del frontend
        persona_serializer=PersonaSerializer(data)
        #valido si el serializer es valido
        if persona_serializer.is_valid():
            #entonces guardo la persona
            persona_serializer.save()
            #la retorno
            return Response(persona_serializer.data)
        #sino arrojo el error
        return Response(persona_serializer.errors)
    
#en django rest PUT es para editar en ves de POST
@api_view(['GET','PUT'])
def Persona_detail_api_view(request, pk=None): #pk=none es para que sea opcional que coloquen el pk en la llamada
    if request.method =='GET':
        persona=Persona.objects.filter(id=pk).first() 
        persona_serializer =PersonaSerializer(persona)   
        return Response(persona_serializer.data)
    elif request.method=='PUT':
     data=request.data #datos que vienen del frontend que voy a actualizar
     #luego  se consulta por pk
    persona=Persona.objects.filter(id=pk).first() 
      #se manda el objeto al serializer ,mas los datos actualizados
    persona_serializer = PersonaSerializer(persona,data)
    #valido
    if persona_serializer.is_valid():
        persona_serializer.save()
        return Response(persona_serializer.data)
    return Response(persona_serializer.errors)
