from django.db import models
from django.contrib.auth.models import User
class Jugador(models.Model):
    OPCIONES_CATEGORIA = [
        ('PREBEN', 'Prebenjamín'),
        ('BEN', 'Benjamín'),
        ('ALE', 'Alevín'),
        ('INF', 'Infantil'),
        ('CAD', 'Cadete'),
        ('JUV', 'Juvenil'),
        ('SEN', 'Sénior')
    ]
    OPCIONES_SUBCATEGORIA = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        # Puedes agregar más si es necesario
    ]
    OPCIONES_EQUIPO = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]
    nombre = models.CharField(max_length=100)
    p_apellido = models.CharField(max_length=100, null=True)
    s_apellido = models.CharField(max_length=100, blank = True)   
    categoria = models.CharField(max_length=20, choices = OPCIONES_CATEGORIA, default='CAD')
    subcategoria = models.CharField(max_length=6, choices =OPCIONES_SUBCATEGORIA, default='A')
    equipo = models.CharField(max_length=10, choices=OPCIONES_EQUIPO, default = "M")
    posicion = models.CharField(max_length=50)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to ='jugadores/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} {self.p_apellido} {self.s_apellido} "

class Carpeta(models.Model):
    jugador = models.ForeignKey(Jugador, related_name ='carpetas', on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 50)
    carpeta_padre = models.ForeignKey('self', on_delete = models.CASCADE, null=True, blank = True, related_name='subcarpetas')
    
    def __str__(self):
        return f"{self.nombre} {self.jugador.nombre}"
    
class PDF (models.Model):
    carpeta = models.ForeignKey(Carpeta, related_name='pdfs', on_delete = models.CASCADE, null=True, blank = True)
    archivo = models.FileField(upload_to='pdfs')
    descripcion = models.CharField(max_length=255, blank=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(max_length=500, blank=True, null=True)
    def save(self, *args, **kwargs):
        if not self.nombre:
            self.nombre = self.archivo.name.split('/')[-1]
        if not self.url:
            self.url = self.archivo.url
            
        super().save(*args, **kwargs)
    def __str__(self):
        return f"{self.nombre} - {self.carpeta.nombre}"
   
   
class Evento (models.Model):
    
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    equipo1 = models.CharField(max_length= 45, default='Portuense F.C.')
    equipo2 = models.CharField(max_length=45,default='')

    
    def __str__(self):
        return  f"{self.equipo1} VS {self.equipo2}"
                                   
                                   