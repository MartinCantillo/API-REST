from rest_framework import  serializers

from .models import Persona
class PersonaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Persona
        fields ='__all__'
    #metodo para personalizar los datos que quiero que se representen o se envien al frontend
    #con el metodo to_representation, SOLO PARA REPRESENTAR , PARA GUARDAR EDITAR Y ELIMINAR Se usa fields por defecto lo usa django rest
    def to_representation(self, instance): #instante es  el diccionario que traigo de la consulta
        return {
          'nombre':instance['nombre'], #asi accedo a las llaves del diccionario
          'apellido' :instance['apellido'],
        }        
'''
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
     
 '''        