from rest_framework import  serializers

from .models import Persona

#NOTA: Para cada crud de una entidad es mejor tener un serializador para mas flexibilidad y modularidad
class PersonaSerializer(serializers.ModelSerializer):
    class Meta :
        model = Persona
        fields ='__all__'
        '''
    #metodos personalizados del serializer
    #se utiliza para crear y guardar una nueva instancia de la clase Persona 
    def create(self,validated_data):     
        #validated_data permite pasar todos los campos validados 
        #como argumentos de palabra clave para inicializar la instancia de la persona.         
        persona=Persona(**validated_data)
        #Establecimiento de la contraseña:
        persona.set_password(validated_data['password'])
        persona.save()
        return persona

'''


 #Serializer para listar (GET)
class PersonasListSerializer(serializers.ModelSerializer):
    class Meta :
        Model :Persona 
        #Como es para mostrar datos especificos no coloco field sino to_representation
    #metodo para personalizar los datos que quiero que se representen o se envien al frontend
    #con el metodo to_representation, SOLO PARA REPRESENTAR , PARA GUARDAR EDITAR Y ELIMINAR Se usa fields por defecto lo usa django rest
    def to_representation(self, instance): #instante es  el diccionario que traigo de la consulta
       #en la consulta o query hay que especificarle los datos a extraer si es .all.value('nombre','apellido')
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