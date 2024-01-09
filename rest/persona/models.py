from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre= models.CharField(max_length=255)
    apellido= models.CharField(max_length =255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    def __str__(self) -> str:
     return f'Persona: Id={self.id}, Nombre={self.nombre}, Apellido={self.apellido}, Email={self.email}: password{self.password}'