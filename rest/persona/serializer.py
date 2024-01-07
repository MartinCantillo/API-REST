from rest_framework import  serializers

from .models import Persona
class PersonaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Persona
        fields ='__all__'
    

 #Para serializers que no dependen del modelo    
class TestPersonaSerializer(serializers.Serializer):
    #defino los campos del serializaer
     nombre= serializers.CharField(max_length=255)
     apellido= serializers.CharField(max_length =255)
     email= serializers.CharField(max_length=255)
     cargo= serializers.CharField(max_length =255)

     #Puedo agregar validaciones en los campos

     def validate_nombre(self, value):
         print(value)
         return value
     def validate_apellido(self, value):
         print(value)
         return value
     def validate_email(self, value):
         print(value)
         return value
     def validate_cargo(self, value):
         print(value)
         return value
     